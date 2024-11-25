#include <unistd.h>

int main()
{
	const char* message = "Hi syscall!\n";
	ssize_t bytes_writ = write(1,message,16);
	return 0;
}
