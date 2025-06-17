import argparse
import hydra
from loguru import logger
from omegaconf import DictConfig, OmegaConf
from pathlib import Path
from tqdm import tqdm
from terasim.logger.infoextractor import InfoExtractor
from terasim.simulator import Simulator

from terasim_nde_nade.envs import NADEWithAV
from terasim_nde_nade.vehicle import NDEVehicleFactory
from terasim_nde_nade.vru import NDEVulnerableRoadUserFactory





def main(config_path: str) -> None:
    config = OmegaConf.load(config_path)
    base_dir = Path(config.output.dir) / config.output.name / "raw_data" / config.output.nth
    base_dir.mkdir(parents=True, exist_ok=True)
    assert "AV_cfg" in config.environment.parameters, "AV_cfg is not in the config file"
    env = NADEWithAV(
        av_cfg = config.environment.parameters.AV_cfg,
        vehicle_factory=NDEVehicleFactory(cfg=config.environment.parameters),
        vru_factory=NDEVulnerableRoadUserFactory(cfg=config.environment.parameters),
        info_extractor=InfoExtractor, 
        log_flag=True,
        log_dir=base_dir,
        warmup_time_lb=599,
        warmup_time_ub=600,
        run_time=1200,
        configuration=config.environment.parameters,
    )

    dir_path = Path(__file__).parent
    sim = Simulator(
        sumo_net_file_path=config.input.sumo_net_file,
        sumo_config_file_path=config.input.sumo_config_file,
        num_tries=10,
        gui_flag=config.simulator.parameters.gui_flag,
        realtime_flag=config.simulator.parameters.realtime_flag,
        output_path=base_dir,
        sumo_output_file_types=["fcd_all", "collision", "tripinfo"],
        additional_sumo_args=["--device.bluelight.explicit","true"],
    )
    sim.bind_env(env)

    terasim_logger = logger.bind(name="terasim_nde_nade")
    terasim_logger.info(f"terasim_nde_nade: Experiment started")

    sim.run()


if __name__ == "__main__":
    # Get all yaml files in config_yamls directory
    config_dir = Path(__file__).parent / "config_yamls"
    yaml_files = sorted(config_dir.glob("*.yaml"), key=lambda x: int(''.join(filter(str.isdigit, x.stem)) or '0'))
    # yaml_files = ["test_config.yaml"]
    
    # Run experiments for each yaml file
    for yaml_file in tqdm(yaml_files):
        print(yaml_file)
        logger.info(f"Running experiment with config: {yaml_file}")
        try:
            main(str(yaml_file))
        except Exception as e:
            logger.error(f"Error running {yaml_file}: {e}")
            yaml_file.unlink()  # Delete the yaml file
            continue
    main()
