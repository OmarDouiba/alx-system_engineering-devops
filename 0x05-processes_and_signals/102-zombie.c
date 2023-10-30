#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int infinite_while(void);

/**
 * main - function that creates 5 zombie processes
 * Return: always 0
 */

int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid != 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();
}

/**
 * infinite_while - funtion that prevents the parent processe from returning
 * Return: always 0
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
