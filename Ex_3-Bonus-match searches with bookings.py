# Exercise3/Bonus exercise: Match searches with bookings 

# Data preprocessing for matching:

booking_dest=booking[['dep_port','arr_port']]# extract clolumns 'dep_port' and 'arr_port' from the 'booking' data 
booking_dest['booking']=1# add a column called 'booking'
booking_dest=booking_dest.rename(columns={'dep_port':'Origin','arr_port':'Destination'})# rename columns for merging


# the 1st method to match: by unique values of the rows in the search data; in the new column 'booking':=1 if matched and =0 if not

result = search.drop_duplicates().merge(booking_dest.drop_duplicates(),on=['Origin','Destination'], how='left')
result= result.fillna(0)# substitue NA by 0 in the column 'booking'

# the 2nd method to match: by each row in the 'search' data, and no any row in 'booking' data is used twice.

booking_dest['X']=booking_dest.groupby(['Origin','Destination']).cumcount()+1
search['X']=search.groupby(['Origin','Destination']).cumcount()+1
result1= pd.merge(search,booking_dest,how='left',on=['Origin','Destination','X'])
del result1['X']
result1=result1.fillna(0)