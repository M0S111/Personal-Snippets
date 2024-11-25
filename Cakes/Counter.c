#include <stdio.h>
/* print the numbers from 1 to i */
int
main(int argc, char **argv){

	int i;
	
	puts("Select range...\n");
	
	scanf("%d",&i);
	
	printf("Now I will count from 1 to %d\n",i);
	
	for(int x = 1; x <= i; x++) {
		printf("%d\n",x);
	}
	return 0;
}
