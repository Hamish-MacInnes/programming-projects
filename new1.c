#include <stdio.h>
// #include <ncurses.h>

int screenSetUp();

int main()
{
	char str[100];
	
  printf ("hello, world \n");
  
  printf( "What is your name? \n");
  scanf("%s", str );
  
  printf("So your name is ");
  puts(str);
  printf("?");
  
  return 0;
 
}

// int screenSetUp
// {
//	initscr();
//	printw("Hello, World");
//	noecho();
//	refresh();
// }
