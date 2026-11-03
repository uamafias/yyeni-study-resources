"""Units and clocks: explicit conversions, including square/cubic scale factors."""
import re
from .topic_teaching import *
from .family_number_b import _LMC, _AV

LABELS={
'nssco_metric_units_conversions':{1:'Converting length, mass and capacity',2:'Converting area and volume',3:'Converting speed units',4:'Converting compound units'},
'nssco_time_clocks_timetables':{1:'Finding a duration across an hour',2:'Finding a duration in hours and minutes',3:'Finding a clock time',4:'Decimal hours and latest departure',5:'Combining journeys and a wait'},
}


def clock_minutes(text):
    h,m=map(int,text.split(':'));return h*60+m


def durations(question):
    return [int(a or 0)*60+int(b or c or 0) for a,b,c in re.findall(r'(?:(\d+) hours?(?: (\d+) minutes?)?|(\d+) minutes?)',question)]


def content(p):
    if p.generator_id not in LABELS:return None
    m=p.machine;t=m['task'];lines=[]
    if p.generator_id=='nssco_metric_units_conversions':
        if t in ('convert','convert_area_volume'):
            table=_LMC if t=='convert' else _AV
            matches=[(F(f),a==m['from']) for a,b,f,_ in table if (a,b)==(m['from'],m['to']) or (b,a)==(m['from'],m['to'])]
            if len(matches)!=1:raise ValueError((m,matches))
            f,forward=matches[0];v=F(m['value']);factor=f if forward else 1/f
            lines=[f'{q(v)}\\times{q(factor)}={q(v*factor)}']
            e=f'The starting quantity is ${q(v)}$ {m["from"]}, and the requested unit is {m["to"]}. The conversion multiplier in this direction is ${q(factor)}$. '+('Area uses the square of the length conversion and volume uses its cube. A litre equals $1000$ cubic centimetres and a cubic metre is $1000$ litres. ' if t=='convert_area_volume' else 'Use units from the same quantity: length, mass or capacity. ')+('Multiply to count more smaller units.' if factor>1 else 'Divide when expressing the same quantity in larger units.' if factor<1 else 'These two units represent equal amounts, so the number is unchanged.')
        elif t=='speed_conversion':
            v=F(m['kmh'] if m['to_ms'] else m['ms']);factor=F(5)/18 if m['to_ms'] else F(18)/5
            lines=[r'1\text{ km/h}='+frac(1000,3600)+r'\text{ m/s}',f'{q(v)}\\times{q(factor)}={q(v*factor)}']
            e=f'The given speed is ${q(v)}$ '+('km/h' if m['to_ms'] else 'm/s')+'. One kilometre is $1000$ metres and one hour $3600$ seconds. Therefore convert km/h to m/s by dividing by $3.6$, or reverse the conversion by multiplying by $3.6$. Both the distance and time units change.'
        else:
            v=F(re.search(r'\$([\d.]+)',p.question)[1])
            if t in ('density','density_back'):
                factor=F(1000) if t=='density' else F(1)/1000
                lines=[r'1\text{ g}=0.001\text{ kg}',r'1\text{ cm}^3=0.000001\text{ m}^3',r'1\text{ g/cm}^3='+frac('0.001','0.000001')+r'\text{ kg/m}^3',f'{q(v)}\\times{q(factor)}={q(v*factor)}']
                e=f'The given density is ${q(v)}$ in the stated mass-per-volume unit. Convert numerator mass and denominator volume separately: a cubic-centimetre conversion cubes the length factor. Their quotient makes $1$ g/cm$^3=1000$ kg/m$^3$. '+('Multiply' if t=='density' else 'Divide')+' the given density by $1000$ in this direction.'
            else:
                lines=[label('Converted amount per original time')+f'={q(v)}\\times1000={q(v*1000)}',label('Requested rate')+'='+frac(f'{q(v)}\\times1000',60)]
                e=f'The given rate is ${q(v)}$ '+('litres per minute' if t=='litres_per_min' else 'kilometres per hour')+'. Multiply by $1000$ to convert '+('litres to millilitres' if t=='litres_per_min' else 'kilometres to metres')+', then divide by $60$ because one '+('minute contains 60 seconds' if t=='litres_per_min' else 'hour contains 60 minutes')+'. A larger number of time units in the denominator reduces the amount per one time unit.'
    else:
        if t in ('duration_minutes','duration_hours_minutes'):
            start,end=clock_minutes(m['start']),clock_minutes(m['end']);total=(end-start)%1440
            lines=[label('Start minutes after midnight')+f'={m["start"].split(":")[0]}\\times60+{int(m["start"].split(":")[1])}={start}',label('End minutes after midnight')+f'={end}',label('Elapsed minutes')+f'={end}-({start})'+('+1440' if end<start else '')+f'={total}']
            if t=='duration_hours_minutes':lines.append(f'{total}=60\\times{total//60}+{total%60}')
            e=f'The start is {m["start"]} and end {m["end"]}. Convert both to minutes after midnight before subtracting. An hour has $60$ minutes, not $100$; if arrival is after midnight, add one day ($1440$ minutes) to the later reading. The duration here is ${total}$ minutes. Divide by $60$ for whole hours and retain the remaining minutes when requested.'
        elif t=='hours_to_hm':
            v=F(m['hours']);h=v//1;minutes=(v-h)*60;lines=[f'{q(v)}={h}+{q(v-h)}',label('Fractional-hour minutes')+f'={q(v-h)}\\times60={q(minutes)}']
            e=f'The decimal duration is ${q(v)}$ hours. Its whole-hours part is ${h}$; the remaining ${q(v-h)}$ is a fraction of an hour, not a minute count. Multiply that fraction by $60$ to obtain ${q(minutes)}$ minutes, then combine with the whole hours.'
        elif t=='hm_to_decimal':
            h,mi=m['h'],m['m'];lines=[label('Hours')+f'={h}+'+frac(mi,60)+'='+q(h+F(mi)/60)]
            e=f'There are ${h}$ whole hours and ${mi}$ minutes. Minutes are sixtieths of an hour, so divide ${mi}$ by $60$ and add the whole hours. Writing the minute count after a decimal point would wrongly use hundredths.'
        else:
            times=re.findall(r'\$(\d{2}:\d{2})\$',p.question);parts=durations(p.question)
            if t in ('total_time','arrival_time'):
                if len(parts)!=3:raise ValueError((t,parts))
                total=sum(parts);lines=[label('Total minutes')+'='+'+'.join(map(str,parts))+f'={total}',f'{total}=60\\times{total//60}+{total%60}']
                e=f'The first journey, wait and second journey last ${parts[0]}$, ${parts[1]}$ and ${parts[2]}$ minutes. Count the wait once and include both journeys. '
                if t=='arrival_time':
                    start=clock_minutes(times[0]);lines.append(label('Arrival minutes after midnight')+f'={start}+{total}={start+total}');e+=f'The departure is {times[0]}; add the total duration to this clock time, carrying every 60 minutes into an hour and wrapping after midnight.'
                else:e+='The question asks for elapsed time, so give the total duration in hours and minutes rather than a clock reading.'
            else:
                start=clock_minutes(times[0]);duration=parts[0];subtract=t in ('latest_departure','early_midnight');signed=-duration if subtract else duration;result=(start+signed)%1440
                lines=[label('Given clock in minutes')+f'={start}',label('Requested clock in minutes')+f'={start}+({signed})={start+signed}',label('Within a 24-hour day')+f'={result}']
                e=f'The given clock reading is {times[0]}, or ${start}$ minutes after midnight, and the duration is ${duration}$ minutes. '+('Subtract because the required event is earlier than the stated clock reading.' if subtract else 'Add because the arrival or late departure is later than the stated reading.')+' Convert back using 60 minutes per hour. A negative or over-1440 total wraps to the adjacent day; write the resulting time with two hour and two minute digits.'
    return finish(p,lines,e)
