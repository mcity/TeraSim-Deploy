import requests
import json
import time


def get_av_state(base_url, simulation_id):
    av_route_response = requests.get(f"{base_url}/av_route/{simulation_id}")
    state_response = requests.get(f"{base_url}/simulation/{simulation_id}/state")
    state_json = state_response.json()
    av_state = state_json["agent_details"]["vehicle"]["AV"]
    return {
        "state": av_state,
        "route": av_route_response.json()
    }



def run_simulation(config_file="test_config.yaml", auto_run=False, initialize_timeout=10, tick_timeout=1):
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

    start_time = time.time()
    while True:
        # Get simulation status
        try:
            status_response = requests.get(f"{base_url}/simulation_status/{simulation_id}")
            # print(f"Simulation status: {status_response.json()}")
            # Break if simulation is waiting for tick
            if status_response.json()["status"] == "wait_for_tick":
                break
            if time.time() - start_time > initialize_timeout:  # 10 seconds timeout
                print("Simulation initialization timeout, stopping...")
                requests.post(f"{base_url}/simulation_control/{simulation_id}", json={"command": "stop"})
                raise TimeoutError("Simulation initialization timeout")
        except Exception as e:
            print(f"Simulation status not ready: {e}")
            time.sleep(0.01)
        
    # Get AV state
    av_state = get_av_state(base_url, simulation_id)
    
    while True:
        # Tick simulation to advance one step
        tick_response = requests.post(f"{base_url}/simulation_tick/{simulation_id}")
        # get simulation status
        start_time = time.time()
        while True:
            status_response = requests.get(f"{base_url}/simulation_status/{simulation_id}")
            if status_response.json()["status"] == "ticked" or status_response.json()["status"] == "finished":
                break
            if time.time() - start_time > tick_timeout:
                print("Simulation stuck for more than 1 second, stopping...")
                requests.post(f"{base_url}/simulation_control/{simulation_id}", json={"command": "stop"})
                return {"error": "Simulation timeout"}
            time.sleep(0.01)
        state_response = requests.get(f"{base_url}/simulation/{simulation_id}/state")
        # print(f"Simulation state: {state_response.json()}")
        if status_response.json()["status"] == "finished":
            break
    
    # Get simulation results
    result_response = requests.get(f"{base_url}/simulation_result/{simulation_id}")
    return result_response.json()

if __name__ == "__main__":
    result = run_simulation()
    print(f"Final simulation result: {result}")
