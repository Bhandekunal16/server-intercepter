from application import Application


class Module:
    @staticmethod
    def main():
        print("Welcome to the server interceptor!")
        while True:
            print("\nChoose an option:")
            print("0) Exit")
            print("1) Scan HTTP server on device")
            print("2) Run Node application with path")
            print("3) List currently open ports")
            print("4) Bind HTTP server to all interfaces")

            try:
                user_input = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if Module.process(user_input):
                print("Exiting...")
                break

    @staticmethod
    def process(choice: int):
        if choice == 0:
            return True
        elif choice == 1:
            Application.scan_http_server()
        elif choice == 2:
            path = input("Enter the path to the Node.js entry file: ")
            Application.node_runner(path)
        elif choice == 3:
            Application.list_open_ports()
        elif choice == 4:
            try:
                port = int(input("Enter the port to bind (e.g. 8080): "))
                path = input("Enter the path to the directory: ")
                Application.local_server_binder(port, path)
            except ValueError:
                print("Port must be a number.")
        else:
            print("Invalid input. Please choose a valid option.")

        return False


Module.main()
