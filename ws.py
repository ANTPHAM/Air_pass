import pandas as pd
import web
import json
       
urls = (
    '/(.*)', 'airport'
)
app = web.application(urls, globals())

class airport:        
    def GET(self, n):
        if not n: 
            n = '10'
        n = int(n);

        if n < 0: return "invalid input"

        print "input: %d"%(n)
        
        Chunksize=100000 # to work on a sample
        booking = pd.read_csv('bookings.csv', sep ='^', iterator=True,chunksize= Chunksize, low_memory=False)
        booking= pd.DataFrame(booking.get_chunk(Chunksize))
        booking.head(2)

        booking_2013=booking.loc[booking["year"] ==2013,['arr_port','pax']]
        booking_top=booking_2013.groupby('arr_port',as_index=False)['pax'].sum()
        result=booking_top.sort_values(['pax'],ascending=False).head(n)
        
        print result

        return pd.DataFrame.to_json(result)

if __name__ == "__main__":
    app.run()