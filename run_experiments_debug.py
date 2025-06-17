import argparse
import hydra
from loguru import logger
from omegaconf import DictConfig, OmegaConf
from pathlib import Path

from terasim.logger.infoextractor import InfoExtractor
from terasim.simulator import Simulator

from terasim_nde_nade.envs import NADEWithAV
from terasim_nde_nade.vehicle import NDEVehicleFactory
from terasim_nde_nade.vru import NDEVulnerableRoadUserFactory

test_config_path = "test_config.yaml"
config = OmegaConf.load(test_config_path)


base_dir = Path(config.output.dir) / config.output.name / "raw_data" / config.output.nth
base_dir.mkdir(parents=True, exist_ok=True)


def main() -> None:
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

    try:
        sim.run()
    except Exception as e:
        terasim_logger.exception(
            f"terasim_nde_nade: Running error catched"
        )


if __name__ == "__main__":
     main()
