char *gnl(int fd)
{
	char buf[1000000];
	char *line;
	int i = 0;
	line = (char *)malloc(100000);
	while (i < 100000)
	{
		buf[i] = 0;
		line[i] = 0;
		i++;
	}
	int i = 0;
	while(read(fd, &buf[i], 1) != -1 && buf[i] != '\n' && buf[i] != '\0')
		i++;
	int j = 0;
	while(j < i)
	{
		line[j] = buf[j];
		j++;
	}
	line[j] = '\0';
	return(line);
}
