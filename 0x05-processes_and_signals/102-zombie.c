#include <stdio.h>
#include <unistd.h>
int infinite_while(void);
/**
 * main - PID
 *
 * Return: Always 0.
 */
int main(void)
{
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	for (i = 0; i < 5; i++)
		infinite_while();

	return (0);
}
/**
 * infinite_while - Sleep
 *
 * Return: 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
