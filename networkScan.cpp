#include <iostream>
#include <cstdlib>

int main()
{
    std::string baseIp = "10.2.1.";

    for (int i = 1; i < 255; ++i)
    {
        std::string ip = baseIp + std::to_string(i);
        std::string command = "ping -c 1 -W 1 " + ip + " > /dev/null";
        int response = system(command.c_str());

        if (response == 0)
        {
            std::cout << "Host " << ip << " is up.\n";
        }
    }

    return 0;
}
