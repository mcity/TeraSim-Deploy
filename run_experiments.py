import requests
import json
import time

def run_simulation(config_file="test_config.yaml", auto_run=False):
    """
    Run simulation and provide HTTP API interface calls
    
    Args:
        config_file (str): Path to configuration file
        auto_run (bool): Whether to run simulation automatically
    
    Returns:
        dict: Simulation results
    """
    base_url = "http://localhost:8000"
    
    # Start simulation
    start_response = requests.post(
        f"{base_url}/start_simulation",
        json={
            "config_file": config_file,
            "auto_run": auto_run
        }
    )
    simulation_id = start_response.json()["simulation_id"]
    
    # Get simulation status
    status_response = requests.get(f"{base_url}/simulation_status/{simulation_id}")
    print(f"Simulation status: {status_response.json()}")
    
    # Get AV route
    route_response = requests.get(f"{base_url}/av_route/{simulation_id}")
    print(f"AV route: {route_response.json()}")
    
    if not auto_run:
        # Manually execute one simulation step
        tick_response = requests.post(f"{base_url}/simulation_tick/{simulation_id}")
        print(f"Simulation tick result: {tick_response.json()}")
    
    # Get simulation state
    state_response = requests.get(f"{base_url}/simulation/{simulation_id}/state")
    print(f"Simulation state: {state_response.json()}")
    
    # Stop simulation
    stop_response = requests.post(
        f"{base_url}/simulation_control/{simulation_id}",
        json={"command": "stop"}
    )
    print(f"Stop simulation result: {stop_response.json()}")
    
    # Get simulation results
    result_response = requests.get(f"{base_url}/simulation_result/{simulation_id}")
    return result_response.json()

if __name__ == "__main__":
    result = run_simulation()
    print(f"Final simulation result: {result}")
