# Import Meteostat library and dependencies
from datetime import datetime
import pandas as pd
from meteostat import Point, Hourly, Stations

class WeatherData():
    '''Class for pulling weather data from meteostat for ETL into data warehouse or pulling only Dallas for
    prediction purposes
    
    For documentation related to meteostat library see: https://dev.meteostat.net/python/
    
    Methods
    -------
    build_obs_df()
        For creating the fact table/training data
    get_station_list()
        For creating StationDim in the data warehouse
    
    Attributes
    ----------
    start_date: datetime
        beginning of date range to pull from meteostat library
    end_date: 
        end of date range to pull from meteostat library
    '''
    def __init__(self, start_date, end_date, dallas_flag=None):
        '''        
        Parameters
        ----------
        start_date: str, YYYY-MM-DD
            Start of the range for pulling data
        end_date: str, YYYY-MM-DD HH:MM
            End of the range for pulling data
        dallas_flag: str, Dallas or None, default None
            If pulling entire DFW/OK region for loading into data warehouse, leave None
            If pulling just Dallas for prediction/testing, use Dallas
        
        Notes
        -----
        To use today's date as end of range use `str(datetime.today())`

        Example
        -------
        >>> ETL_build = WeatherData('2022-01-01', '2022-11-30 23:59')
        >>> stations_fact = ETL_build.build_obs_df()
        >>> stations_dim = ETL_build.get_station_list()
        '''
        self.start_date = datetime.fromisoformat(start_date)
        self.end_date = datetime.fromisoformat(end_date)
        self.dallas_flag = dallas_flag
    
    def build_obs_df(self):
        '''Takes provided `start_date` and `end_date` and pulls observations for that date range
        exclusive of the end date
        
        Returns
        -------
        DataFrame of observations for stations/time periods requested
        
        Note
        ----
        For column name definitions see: https://dev.meteostat.net/python/hourly.html#data-structure
        '''
        # Get hourly data
        if self.dallas_flag:
            station = '72259'
        else:
            station =self.get_station_list().index.to_list()
        data = Hourly(station, self.start_date, self.end_date)
        data = data.fetch()
        return data.reset_index()
    
    def get_station_list(self):
        '''Provides station attributes for entire DFW/Oklahoma region for loading into StationsDim'''
        stationsclass = Stations()
        stations = stationsclass.nearby(32.9, -97.0333, 196126.868894258)
        stations_df = stations.fetch()
        return stations_df