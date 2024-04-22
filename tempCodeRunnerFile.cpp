
    int option;
    printf("Chon thuat toan: \n");
    printf("1. GTS1\n");
    printf("2. GTS2\n");
    scanf("%d", &option);

    if (option == 1) {
        
        docfile_gts1(f,ary,n,start_village_gts1);
    
    	mincost_GTS1(start_village_gts1);
    	printf("\n\nMinimum cost is %d\n", cost);
    	
    } else if (option == 2) {