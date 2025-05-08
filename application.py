import subprocess


class Support:
    def process_run_time(process: list, errorInp: str):
        try:
            subprocess.run(process)
            return True
        except FileNotFoundError:
            print(
                f"{errorInp} not found. Please ensure it is in the correct directory."
            )
            return False
        except PermissionError:
            print(
                f"Permission denied. Please check your permissions to run {errorInp}."
            )
            return False
        except KeyboardInterrupt:
            print("Process interrupted by user.")
            return False
        except Exception as e:
            print(f"Error running {errorInp}: {e}")
            return False


class Application:
    @staticmethod
    def scan_http_server():
        Support.process_run_time(["./maintainer.bin"], "maintainer.bin")
        
    @staticmethod
    def scan_wifi_network():
        Support.process_run_time(["./networkScan.bin"], "networkScan.bin")

    @staticmethod
    def node_runner(entryPoint: str):
        Support.process_run_time(["node", entryPoint], "entryPoint")

    @staticmethod
    def list_open_ports():
        Support.process_run_time(["lsof", "-i", "-P", "-n"], "lsof")

    @staticmethod
    def local_server_binder(port: int, path: str):
        try:
            subprocess.run(["python3", "-m", "http.server", str(port)], cwd=path)
            return True
        except FileNotFoundError:
            print("entryPoint not found. Please ensure it is in the correct directory.")
            return False
        except PermissionError:
            print("Permission denied. Please check your permissions to run entryPoint.")
            return False
        except KeyboardInterrupt:
            print("Process interrupted by user.")
            return False
        except Exception as e:
            print(f"Error running entryPoint: {e}")
            return False
