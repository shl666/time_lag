import datetime
import pytz
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-tz1", help="the 1st timezone, e.g. 'Asia/Shanghai' ", 
                    type=str, default='Asia/Shanghai')
parser.add_argument("-tz2", help="the 2nd timezone, e.g. 'America/Los_Angeles' ",
                    type=str, default='America/Los_Angeles')
parser.add_argument("-tz1_time", help="the time need to be converted, e.g. '2018-12-28 4:00' ",
                    type=str, default='2018-12-28 4:00')
args = parser.parse_args()


def timezone_convertor(tz1='Asia/Shanghai', tz2='America/Los_Angeles', tz1_time='2018-12-28 4:00'):
    
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    tz1 = pytz.timezone(tz1)
    tz2 = pytz.timezone(tz2)
    
    tz1_loctime = tz1_time.replace('-',' ').replace(':',' ').split()
    input_time = datetime.datetime(int(tz1_loctime[0]), int(tz1_loctime[1]), int(tz1_loctime[2]), 
                                   int(tz1_loctime[3]), int(tz1_loctime[4]))
    
    tz1_dt = tz1.localize(input_time)
    tz2_dt = tz1_dt.astimezone(tz2)
    tz2_loctime = tz2_dt.strftime(fmt).replace('-',' ').replace(':',' ').split()
    tz2_weekday = datetime.datetime(int(tz2_loctime[0]), int(tz2_loctime[1]), int(tz2_loctime[2]), 
                                    int(tz2_loctime[3]), int(tz2_loctime[4])).strftime('%A')
    tz2_loctime = tz2_dt.strftime(fmt)+ ' '+ tz2_weekday
    return tz2_loctime

if __name__ == '__main__':
    
    tz2_time = timezone_convertor(args.tz1, args.tz2, args.tz1_time)
    print(tz2_time)