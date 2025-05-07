#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("starting the maintainer!\n");
    printf("scaning of the http server\n");

    const char *static_port[6] = {"8080", "3000", "443", "80", "8888"};
    int stop = sizeof(static_port) / sizeof(static_port[0]);

    for (int i = 0; i < stop; i++)
    {
        char command[256];

        snprintf(command, sizeof(command),
                 "ss -tuln | grep -q ':%s '", static_port[i]);

        int opencloseflag = system(command);

        if (opencloseflag == 0)
        {
            printf("detect http server on port %s\n", static_port[i]);
            printf("getting the process information for %s\n", static_port[i]);

            char process_command[256];
            snprintf(process_command, sizeof(process_command),
                     "lsof -i :%s\n", static_port[i]);
            system(process_command);
        }
    }

    for (int i = 3001; i < 65535; i++)
    {
        char str[12];
        snprintf(str, sizeof(str), "%d", i);
        char command[256];

        snprintf(command, sizeof(command),
                 "ss -tuln | grep -q ':%s '", str);
        int opencloseflag = system(command);
        if (opencloseflag == 0)
        {
            printf("detect http server on port %s\n", str);
            printf("getting the process information for %s\n", str);
            char process_command[256];
            snprintf(process_command, sizeof(process_command),
                     "lsof -i :%s\n", str);
            system(process_command);
        }
    }

    return 0;
}
