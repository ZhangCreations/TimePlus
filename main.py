# Time+, an application with various measuring capabilities
# Made by Kevin Zhang


from datetime import datetime
from dateutil import relativedelta
from tkinter import *
import TKTable
import time
from calendar import monthrange
import pygame

secondsLeft = 0
TimerHours = 0
TimerMinutes = 0
TimerSeconds = 0
initialHours = 0
initialMinutes = 0
initialSeconds = 0
TimerPauseVar = False
StopwatchHours = 0
StopwatchMinutes = 0
StopwatchSeconds = 0
StopwatchPauseVar = False
RowCounter = 1

pygame.mixer.init(11025)
Alert = pygame.mixer.Sound("Alarm.wav")


def chooseDateCalc():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    def calculations():
        try:
            fromYear = FromYearVar.get()
            fromMonth = months.index(FromMonthVar.get()) + 1
            fromDate = FromDateVar.get()
            fromHour = FromHourVar.get()
            if FromAMPM.get() == 1 and fromHour != 12:
                fromHour += 12
            if FromAMPM.get() == 0 and fromHour == 12:
                fromHour = 0
            fromMinute = FromMinuteVar.get()
            fromSeconds = FromSecondVar.get()
            toYear = ToYearVar.get()
            toMonth = months.index(ToMonthVar.get()) + 1
            toDate = ToDateVar.get()
            toHour = ToHourVar.get()
            if ToAMPM.get() == 1 and toHour != 12:
                toHour += 12
            if ToAMPM.get() == 0 and toHour == 12:
                toHour = 0
            toMinute = ToMinuteVar.get()
            toSeconds = ToSecondVar.get()
            date_1 = datetime(fromYear, fromMonth, fromDate, fromHour, fromMinute, fromSeconds)
            date_2 = datetime(toYear, toMonth, toDate, toHour, toMinute, toSeconds)
            difference = relativedelta.relativedelta(date_2, date_1)
            FromAMPMFormat = FromAMPM.get()
            ToAMPMFormat = ToAMPM.get()
            if ToAMPMFormat == 0:
                ToAMPMFormat = "AM"
            elif ToAMPMFormat == 1:
                ToAMPMFormat = "PM"
            if FromAMPMFormat == 0:
                FromAMPMFormat = "AM"
            elif FromAMPMFormat == 1:
                FromAMPMFormat = "PM"
            date_1 = f'{fromHour}:{"00" if fromMinute is 0 else fromMinute}:' \
                     f'{"00" if fromSeconds is 0 else fromSeconds} {FromAMPMFormat} {months[fromMonth-1]} ' \
                     f'{fromDate}, {fromYear}'
            date_2 = f'{toHour}:{"00" if toMinute is 0 else fromMinute}:' \
                     f'{"00" if toSeconds is 0 else toSeconds} {ToAMPMFormat} {months[toMonth-1]} {toDate}, ' \
                     f'{toYear}'
            ResultsVar.set(f'There are {0 if difference.days is None else  abs(difference.days)} days'
                           f'\n{0 if difference.months is None else abs(difference.months)} months'
                           f'\n{0 if difference.years is None else abs(difference.years)} years'
                           f'\n{0 if difference.hours is None else abs(difference.hours)} hours'
                           f'\n{0 if difference.minutes is None else abs(difference.minutes)} minutes'
                           f'\nand {0 if difference.seconds is None else abs(difference.seconds)} seconds between'
                           f'\n{date_1} and'
                           f'\n{date_2}')
        except:
            ResultsVar.set("There is a error in your input\nPlease try again")

    currenttime = datetime.now()
    DateCalcroot = Toplevel()
    DateCalcPopup = Frame(DateCalcroot)
    From = Label(DateCalcPopup, text="From", font=("Futura", 14))
    FromDateLabel = Label(DateCalcPopup, text="Date:", font=("Futura", 12))
    FromDateVar = IntVar()
    FromDateVar.set(currenttime.day)
    FromDateEntry = Entry(DateCalcPopup, textvariable=FromDateVar, width=24)
    FromMonthVar = StringVar()
    FromMonthVar.set(months[int(currenttime.month) - 1])
    FromMonthLabel = Label(DateCalcPopup, text="Month:", font=("Futura", 12))
    FromMonthOptionMenu = OptionMenu(DateCalcPopup, FromMonthVar, *months)
    FromYearLabel = Label(DateCalcPopup, text="Year:", font=("Futura", 12))
    FromYearVar = IntVar()
    FromYearVar.set(currenttime.year)
    FromYearEntry = Entry(DateCalcPopup, textvariable=FromYearVar, width=24)
    FromHourLabel = Label(DateCalcPopup, text="Hour:", font=("Futura", 12))
    FromHourVar = IntVar()
    FromHourVar.set(12)
    FromHourEntry = Entry(DateCalcPopup, textvariable=FromHourVar, width=24)
    FromAMPM = IntVar()
    FromAMPM.set(1)
    FromAMPMFrame = Frame(DateCalcPopup)
    FromAM = Radiobutton(FromAMPMFrame, text="AM", value=0, variable=FromAMPM)
    FromPM = Radiobutton(FromAMPMFrame, text="PM", value=1, variable=FromAMPM)
    FromMinuteLabel = Label(DateCalcPopup, text="Minute:", font=("Futura", 12))
    FromMinuteVar = IntVar()
    FromMinuteVar.set(0)
    FromMinuteEntry = Entry(DateCalcPopup, textvariable=FromMinuteVar, width=24)
    FromSecondLabel = Label(DateCalcPopup, text="Second:", font=("Futura", 12))
    FromSecondVar = IntVar()
    FromSecondVar.set(0)
    FromSecondEntry = Entry(DateCalcPopup, textvariable=FromSecondVar, width=24)

    To = Label(DateCalcPopup, text="To", font=("Futura", 14))
    ToDateLabel = Label(DateCalcPopup, text="Date:", font=("Futura", 12))
    ToDateVar = IntVar()
    ToSetDay = currenttime.day + 1
    ToSetMonth = currenttime.month
    ToSetYear = currenttime.year
    if not((currenttime.day + 1) in monthrange(currenttime.year, currenttime.month)):
        if ToSetMonth == 12:
            ToSetYear = currenttime.year + 1
            ToSetMonth = 1
            ToSetDay = 1
        else:
            ToSetMonth += 1
            ToSetDay = 1
    ToDateVar.set(ToSetDay)
    ToDateEntry = Entry(DateCalcPopup, textvariable=ToDateVar, width=24)
    ToMonthLabel = Label(DateCalcPopup, text="Month:", font=("Futura", 12))
    ToMonthVar = StringVar()
    ToMonthVar.set(months[int(ToSetMonth) - 1])
    ToMonthOptionMenu = OptionMenu(DateCalcPopup, ToMonthVar, *months)
    ToYearLabel = Label(DateCalcPopup, text="Year:", font=("Futura", 12))
    ToYearVar = IntVar()
    ToYearVar.set(ToSetYear)
    ToYearEntry = Entry(DateCalcPopup, textvariable=ToYearVar, width=24)
    ToHourLabel = Label(DateCalcPopup, text="Hour:", font=("Futura", 12))
    ToHourVar = IntVar()
    ToHourVar.set(12)
    ToHourEntry = Entry(DateCalcPopup, textvariable=ToHourVar, width=24)
    ToAMPM = IntVar()
    ToAMPM.set(1)
    ToAMPMFrame = Frame(DateCalcPopup)
    ToAM = Radiobutton(ToAMPMFrame, text="AM", value=0, variable=ToAMPM)
    ToPM = Radiobutton(ToAMPMFrame, text="PM", value=1, variable=ToAMPM)
    ToMinuteLabel = Label(DateCalcPopup, text="Minute:", font=("Futura", 12))
    ToMinuteVar = IntVar()
    ToMinuteVar.set(0)
    ToMinuteEntry = Entry(DateCalcPopup, textvariable=ToMinuteVar, width=24)
    ToSecondLabel = Label(DateCalcPopup, text="Second:", font=("Futura", 12))
    ToSecondVar = IntVar()
    ToSecondVar.set(0)
    ToSecondEntry = Entry(DateCalcPopup, textvariable=ToSecondVar, width=24)
    titleLabel = Label(DateCalcPopup, text="Date Calculator", font=("Futura", 20))
    calculate = Button(DateCalcPopup, text="Calculate!", command=calculations)

    ResultLabelFrame = LabelFrame(DateCalcPopup)
    ResultsVar = StringVar()
    ResultsVar.set("The result will appear here")
    ResultLabel = Label(ResultLabelFrame, textvariable=ResultsVar, font=("Futura", 14))

    # Grid widgets
    DateCalcroot.title("Date Calculator")
    DateCalcPopup.grid(padx=50, pady=50)
    DateCalcroot.minsize(width=1100, height=300)
    titleLabel.grid(row=1, column=3, sticky=E, columnspan=2)
    From.grid(row=2, column=2)
    FromYearLabel.grid(row=3, column=1, sticky=W)
    FromYearEntry.grid(row=3, column=2, sticky=W)
    FromMonthLabel.grid(row=4, column=1, sticky=W)
    FromMonthOptionMenu.grid(row=4, column=2, sticky=EW, )
    FromDateLabel.grid(row=5, column=1, sticky=W)
    FromDateEntry.grid(row=5, column=2, sticky=W)
    FromHourLabel.grid(row=6, column=1, sticky=W)
    FromHourEntry.grid(row=6, column=2, sticky=W)
    FromAMPMFrame.grid(row=7, column=2, sticky=W)
    FromAM.grid(row=1, column=1, sticky=W)
    FromPM.grid(row=1, column=2, sticky=W)
    FromMinuteLabel.grid(row=8, column=1, sticky=W)
    FromMinuteEntry.grid(row=8, column=2, sticky=W)
    FromSecondLabel.grid(row=9, column=1, sticky=W)
    FromSecondEntry.grid(row=9, column=2, sticky=W)

    To.grid(row=2, column=6)
    ToYearLabel.grid(row=3, column=5, sticky=W)
    ToYearEntry.grid(row=3, column=6, sticky=W)
    ToMonthLabel.grid(row=4, column=5, sticky=W)
    ToMonthOptionMenu.grid(row=4, column=6, sticky=EW)
    ToDateLabel.grid(row=5, column=5, sticky=W)
    ToDateEntry.grid(row=5, column=6, sticky=W)
    ToHourLabel.grid(row=6, column=5, sticky=W)
    ToHourEntry.grid(row=6, column=6, sticky=W)
    ToAMPMFrame.grid(row=7, column=6, sticky=W)
    ToAM.grid(row=1, column=1, sticky=W)
    ToPM.grid(row=1, column=2, sticky=W)
    ToMinuteLabel.grid(row=8, column=5, sticky=W)
    ToMinuteEntry.grid(row=8, column=6, sticky=W)
    ToSecondLabel.grid(row=9, column=5, sticky=W)
    ToSecondEntry.grid(row=9, column=6, sticky=W)

    calculate.grid(row=9, column=8, sticky=W, ipadx=10)
    ResultLabelFrame.grid(row=3, column=8, sticky=W, rowspan=6, padx=30)
    ResultLabel.grid(row=1)

def calculations():
    try:
        fromYear = FromYearVar.get()
        fromMonth = months.index(FromMonthVar.get()) + 1
        fromDate = FromDateVar.get()
        fromHour = FromHourVar.get()
        if FromAMPM.get() == 1 and fromHour != 12:
            fromHour += 12
        if FromAMPM.get() == 0 and fromHour == 12:
            fromHour = 0
        fromMinute = FromMinuteVar.get()
        fromSeconds = FromSecondVar.get()
        toYear = ToYearVar.get()
        toMonth = months.index(ToMonthVar.get()) + 1
        toDate = ToDateVar.get()
        toHour = ToHourVar.get()
        if ToAMPM.get() == 1 and toHour != 12:
            toHour += 12
        if ToAMPM.get() == 0 and toHour == 12:
            toHour = 0
        toMinute = ToMinuteVar.get()
        toSeconds = ToSecondVar.get()
        date_1 = datetime(fromYear, fromMonth, fromDate, fromHour, fromMinute, fromSeconds)
        date_2 = datetime(toYear, toMonth, toDate, toHour, toMinute, toSeconds)
        difference = datetime.timedelta(date_2, date_1)
        FromAMPMFormat = FromAMPM.get()
        ToAMPMFormat = ToAMPM.get()
        if ToAMPMFormat == 0:
            ToAMPMFormat = "AM"
        elif ToAMPMFormat == 1:
            ToAMPMFormat = "PM"
        if FromAMPMFormat == 0:
            FromAMPMFormat = "AM"
        elif FromAMPMFormat == 1:
            FromAMPMFormat = "PM"
        date_1 = f'{fromHour}:{"00" if fromMinute is 0 else fromMinute}:' \
                 f'{"00" if fromSeconds is 0 else fromSeconds} {FromAMPMFormat} {months[fromMonth-1]} ' \
                 f'{fromDate}, {fromYear}'
        date_2 = f'{toHour}:{"00" if toMinute is 0 else fromMinute}:' \
                 f'{"00" if toSeconds is 0 else toSeconds} {ToAMPMFormat} {months[toMonth-1]} {toDate}, ' \
                 f'{toYear}'
        ResultsVar.set(f'There are {0 if difference.days is None else  abs(difference.days)} days'
                       f'\n{0 if difference.months is None else abs(difference.months)} months'
                       f'\n{0 if difference.years is None else abs(difference.years)} years'
                       f'\n{0 if difference.hours is None else abs(difference.hours)} hours'
                       f'\n{0 if difference.minutes is None else abs(difference.minutes)} minutes'
                       f'\nand {0 if difference.seconds is None else abs(difference.seconds)} seconds between'
                       f'\n{date_1} and'
                       f'\n{date_2}')
    except:
        ResultsVar.set("There is an error in your input\nPlease try again")

    currenttime = datetime.now()
    DateCalcroot = Toplevel()
    DateCalcPopup = Frame(DateCalcroot)
    From = Label(DateCalcPopup, text="From", font=("Futura", 14))
    FromDateLabel = Label(DateCalcPopup, text="Days:", font=("Futura", 12))
    FromDateVar = IntVar()
    FromDateVar.set(currenttime.day)
    FromDateEntry = Entry(DateCalcPopup, textvariable=FromDateVar, width=24)
    FromMonthVar = StringVar()
    FromMonthVar.set(months[int(currenttime.month) - 1])
    FromMonthLabel = Label(DateCalcPopup, text="Months:", font=("Futura", 12))
    FromMonthOptionMenu = OptionMenu(DateCalcPopup, FromMonthVar, *months)
    FromYearLabel = Label(DateCalcPopup, text="Years:", font=("Futura", 12))
    FromYearVar = IntVar()
    FromYearVar.set(currenttime.year)
    FromYearEntry = Entry(DateCalcPopup, textvariable=FromYearVar, width=24)
    FromHourLabel = Label(DateCalcPopup, text="Hours:", font=("Futura", 12))
    FromHourVar = IntVar()
    FromHourVar.set(12)
    FromHourEntry = Entry(DateCalcPopup, textvariable=FromHourVar, width=24)
    FromAMPM = IntVar()
    FromAMPM.set(1)
    FromAMPMFrame = Frame(DateCalcPopup)
    FromAM = Radiobutton(FromAMPMFrame, text="AM", value=0, variable=FromAMPM)
    FromPM = Radiobutton(FromAMPMFrame, text="PM", value=1, variable=FromAMPM)
    FromMinuteLabel = Label(DateCalcPopup, text="Minutes:", font=("Futura", 12))
    FromMinuteVar = IntVar()
    FromMinuteVar.set(0)
    FromMinuteEntry = Entry(DateCalcPopup, textvariable=FromMinuteVar, width=24)
    FromSecondLabel = Label(DateCalcPopup, text="Seconds:", font=("Futura", 12))
    FromSecondVar = IntVar()
    FromSecondVar.set(0)
    FromSecondEntry = Entry(DateCalcPopup, textvariable=FromSecondVar, width=24)

    To = Label(DateCalcPopup, text="To", font=("Futura", 14))
    ToDateLabel = Label(DateCalcPopup, text="Days:", font=("Futura", 12))
    ToDateVar = IntVar()
    ToSetDay = currenttime.day + 1
    ToSetMonth = currenttime.month
    ToSetYear = currenttime.year
    if not((currenttime.day + 1) in monthrange(currenttime.year, currenttime.month)):
        if ToSetMonth == 12:
            ToSetYear = currenttime.year + 1
            ToSetMonth = 1
            ToSetDay = 1
        else:
            ToSetMonth += 1
            ToSetDay = 1
    ToDateVar.set(ToSetDay)
    ToDateEntry = Entry(DateCalcPopup, textvariable=ToDateVar, width=24)
    ToMonthLabel = Label(DateCalcPopup, text="Months:", font=("Futura", 12))
    ToMonthVar = StringVar()
    ToMonthVar.set(months[int(ToSetMonth) - 1])
    ToMonthOptionMenu = OptionMenu(DateCalcPopup, ToMonthVar, *months)
    ToYearLabel = Label(DateCalcPopup, text="Years:", font=("Futura", 12))
    ToYearVar = IntVar()
    ToYearVar.set(ToSetYear)
    ToYearEntry = Entry(DateCalcPopup, textvariable=ToYearVar, width=24)
    ToHourLabel = Label(DateCalcPopup, text="Hours:", font=("Futura", 12))
    ToHourVar = IntVar()
    ToHourVar.set(12)
    ToHourEntry = Entry(DateCalcPopup, textvariable=ToHourVar, width=24)
    ToAMPM = IntVar()
    ToAMPM.set(1)
    ToAMPMFrame = Frame(DateCalcPopup)
    ToAM = Radiobutton(ToAMPMFrame, text="AM", value=0, variable=ToAMPM)
    ToPM = Radiobutton(ToAMPMFrame, text="PM", value=1, variable=ToAMPM)
    ToMinuteLabel = Label(DateCalcPopup, text="Minutes:", font=("Futura", 12))
    ToMinuteVar = IntVar()
    ToMinuteVar.set(0)
    ToMinuteEntry = Entry(DateCalcPopup, textvariable=ToMinuteVar, width=24)
    ToSecondLabel = Label(DateCalcPopup, text="Seconds:", font=("Futura", 12))
    ToSecondVar = IntVar()
    ToSecondVar.set(0)
    ToSecondEntry = Entry(DateCalcPopup, textvariable=ToSecondVar, width=24)
    titleLabel = Label(DateCalcPopup, text="Date Calculator", font=("Futura", 20))
    calculate = Button(DateCalcPopup, text="Calculate!", command=calculations)

    ResultLabelFrame = LabelFrame(DateCalcPopup)
    ResultsVar = StringVar()
    ResultsVar.set("The result will appear here")
    ResultLabel = Label(ResultLabelFrame, textvariable=ResultsVar, font=("Futura", 14))

    # Grid widgets
    DateCalcroot.title("Date Calculator")
    DateCalcPopup.grid(padx=50, pady=50)
    DateCalcroot.minsize(width=1100, height=300)
    titleLabel.grid(row=1, column=3, sticky=E, columnspan=2)
    From.grid(row=2, column=2)
    FromYearLabel.grid(row=3, column=1, sticky=W)
    FromYearEntry.grid(row=3, column=2, sticky=W)
    FromMonthLabel.grid(row=4, column=1, sticky=W)
    FromMonthOptionMenu.grid(row=4, column=2, sticky=EW, )
    FromDateLabel.grid(row=5, column=1, sticky=W)
    FromDateEntry.grid(row=5, column=2, sticky=W)
    FromHourLabel.grid(row=6, column=1, sticky=W)
    FromHourEntry.grid(row=6, column=2, sticky=W)
    FromAMPMFrame.grid(row=7, column=2, sticky=W)
    FromAM.grid(row=1, column=1, sticky=W)
    FromPM.grid(row=1, column=2, sticky=W)
    FromMinuteLabel.grid(row=8, column=1, sticky=W)
    FromMinuteEntry.grid(row=8, column=2, sticky=W)
    FromSecondLabel.grid(row=9, column=1, sticky=W)
    FromSecondEntry.grid(row=9, column=2, sticky=W)

    To.grid(row=2, column=6)
    ToYearLabel.grid(row=3, column=5, sticky=W)
    ToYearEntry.grid(row=3, column=6, sticky=W)
    ToMonthLabel.grid(row=4, column=5, sticky=W)
    ToMonthOptionMenu.grid(row=4, column=6, sticky=EW)
    ToDateLabel.grid(row=5, column=5, sticky=W)
    ToDateEntry.grid(row=5, column=6, sticky=W)
    ToHourLabel.grid(row=6, column=5, sticky=W)
    ToHourEntry.grid(row=6, column=6, sticky=W)
    ToAMPMFrame.grid(row=7, column=6, sticky=W)
    ToAM.grid(row=1, column=1, sticky=W)
    ToPM.grid(row=1, column=2, sticky=W)
    ToMinuteLabel.grid(row=8, column=5, sticky=W)
    ToMinuteEntry.grid(row=8, column=6, sticky=W)
    ToSecondLabel.grid(row=9, column=5, sticky=W)
    ToSecondEntry.grid(row=9, column=6, sticky=W)

    calculate.grid(row=9, column=8, sticky=W, ipadx=10)
    ResultLabelFrame.grid(row=3, column=8, sticky=W, rowspan=6, padx=30)
    ResultLabel.grid(row=1)


def chooseTime():
    def Timer1():
        global TimerHours, TimerMinutes, TimerSecond, initialHours, initialMinutes, initialSeconds
        TimerHours = HourVar.get()
        initialHours = TimerHours
        TimerMinutes = MinuteVar.get()
        while TimerMinutes >= 60:
            TimerMinutes -= 60
            TimerHours += 1
        initialMinutes = TimerMinutes
        TimerSecond = SecondsVar.get()
        while TimerSecond >= 60:
            TimerSecond -= 60
            TimerMinutes += 1
        initialSeconds = TimerSecond
        TimerLabelVar.set(f'{TimerHours:0>2}:{TimerMinutes:0>2}:{TimerSecond:0>2}')
        clearButton.grid(row=9, column=6, sticky=E)
        pauseButton.grid(row=9, column=7, sticky=E)
        TimerRoot.update()
        time.sleep(1)
        TimerCount()

    def Timer2():
        global PresetTimes, TimerHours, TimerMinutes, TimerSecond
        PresetTimes = ["1 Minute", "5 Minutes", "10 Minutes", "30 Minutes", "45 Minutes", "1 Hour",
                       "2 Hours", "3 TimerHours", "5 Hours"]
        Time = PresetTimesVar.get()
        if PresetTimes.index(Time) == 0:
            TimerHours = 0
            TimerMinutes = 1
            TimerSecond = 0
        elif PresetTimes.index(Time) == 1:
            TimerHours = 0
            TimerMinutes = 5
            TimerSecond = 0
        elif PresetTimes.index(Time) == 2:
            TimerHours = 0
            TimerMinutes = 10
            TimerSecond = 0
        elif PresetTimes.index(Time) == 3:
            TimerHours = 0
            TimerMinutes = 30
            TimerSecond = 0
        elif PresetTimes.index(Time) == 4:
            TimerHours = 0
            TimerMinutes = 45
            TimerSecond = 0
        elif PresetTimes.index(Time) == 5:
            TimerHours = 1
            TimerMinutes = 0
            TimerSecond = 0
        elif PresetTimes.index(Time) == 6:
            TimerHours = 2
            TimerMinutes = 0
            TimerSecond = 0
        elif PresetTimes.index(Time) == 7:
            TimerHours = 3
            TimerMinutes = 0
            TimerSecond = 0
        elif PresetTimes.index(Time) == 8:
            TimerHours = 5
            TimerMinutes = 0
            TimerSecond = 0
        TimerLabelVar.set(f'{TimerHours:0>2}:{TimerMinutes:0>2}:{TimerSecond:0>2}')
        clearButton.grid(row=9, column=6, sticky=E)
        pauseButton.grid(row=9, column=7, sticky=E)
        TimerRoot.update()
        time.sleep(1)
        TimerCount()

    def TimerCount():
        global TimerHours, TimerMinutes, TimerSecond
        while not (TimerSecond == 0 and TimerMinutes == 0 and TimerHours == 0) and not TimerPauseVar:
            if TimerSecond == 0:
                if TimerMinutes == 0:
                    TimerHours -= 1
                    TimerMinutes += 60
                TimerMinutes -= 1
                TimerSecond += 60
            TimerSecond -= 1
            TimerLabelVar.set(f'{TimerHours:0>2}:{TimerMinutes:0>2}:{TimerSecond:0>2}')
            TimerRoot.update()
            time.sleep(1)
            TimerCount()
        if not TimerPauseVar:
            clearButton.grid_remove()
            pauseButton.grid_remove()
        if TimerSecond == 0 and TimerMinutes == 0 and TimerHours == 0:
            Alert.play()
            time.sleep(2)
            Alert.stop()

    def clear():
        global TimerHours, TimerMinutes, TimerSecond
        TimerHours = 0
        TimerMinutes = 0
        TimerSecond = 0
        TimerLabelVar.set('00:00:00')
        pauseButton.config(text="Pause")

    def pause():
        global TimerHours, TimerMinutes, TimerSecond, TimerPauseVar
        TimerPauseVar = not TimerPauseVar
        if not TimerPauseVar:
            pauseButton.config(text="Pause")
        else:
            pauseButton.config(text="Resume")
        TimerCount()

    # MAIN
    TimerRoot = Toplevel()
    TimerPopup = Frame(TimerRoot)
    # Create widgets
    currenttime = datetime.now()
    TimerLabel = Label(TimerPopup, text="Timer", font=("Futura", 36))
    CustomSetLabel = Label(TimerPopup, text="Custom Set Timer", font=("Futura", 14))
    HourLabel = Label(TimerPopup, text="Hours", font=("Futura", 12))
    HourVar = IntVar()
    HourVar.set(0)
    HourEntry = Entry(TimerPopup, textvariable=HourVar, justify=CENTER, width=10)
    MinuteLabel = Label(TimerPopup, text="Minutes", font=("Futura", 12))
    MinuteVar = IntVar()
    MinuteVar.set(0)
    MinuteEntry = Entry(TimerPopup, textvariable=MinuteVar, justify=CENTER, width=10)
    SecondsLabel = Label(TimerPopup, text="Seconds", font=("Futura", 12))
    SecondsVar = IntVar()
    SecondsVar.set(0)
    SecondsEntry = Entry(TimerPopup, textvariable=SecondsVar, justify=CENTER, width=10)
    ORLabel = Label(TimerPopup, text="OR", font=("Futura", 12))
    PresetLabel = Label(TimerPopup, text="Preset Times", font=("Futura", 14))
    PresetTimes = ["1 Minute", "5 Minutes", "10 Minutes", "30 Minutes", "45 Minutes", "1 Hour",
                   "2 Hours", "3 Hours", "5 Hours"]
    PresetTimesVar = StringVar()
    PresetTimesVar.set("Choose a Time")
    PresetOptionMenu = OptionMenu(TimerPopup, PresetTimesVar, *PresetTimes)
    BeginButton1 = Button(TimerPopup, text="Custom timer!", command=Timer1)
    BeginButton2 = Button(TimerPopup, text="Preset timer!", command=Timer2)
    TimerFrame = LabelFrame(TimerPopup)
    TimerLabelVar = StringVar()
    TimerLabelVar.set("00:00:00")
    TimerValueLabel = Label(TimerFrame, textvariable=TimerLabelVar, font=("Futura", 72))
    clearButton = Button(TimerPopup, text="Clear", font=("Futura", 12), command=clear)
    pauseButton = Button(TimerPopup, text="Pause", font=("Futura", 12), command=pause)

    # Grid widgets
    TimerPopup.grid(padx=50, pady=50)

    TimerLabel.grid(row=1, column=4, columnspan=3, sticky=W)
    CustomSetLabel.grid(row=2, column=2)
    HourEntry.grid(row=3, column=1)
    HourLabel.grid(row=4, column=1)
    MinuteEntry.grid(row=3, column=2)
    MinuteLabel.grid(row=4, column=2)
    SecondsEntry.grid(row=3, column=3)
    SecondsLabel.grid(row=4, column=3)
    BeginButton1.grid(row=5, column=2)
    ORLabel.grid(row=6, column=2)
    PresetLabel.grid(row=7, column=2)
    PresetOptionMenu.grid(row=8, column=2, sticky="ew")
    BeginButton2.grid(row=9, column=2)
    TimerFrame.grid(padx=75, row=2, column=6, rowspan=5, columnspan=3)
    TimerValueLabel.grid(row=1)


def chooseStopwatch2():
    def start():
        global StopwatchHours, StopwatchMinutes, StopwatchSeconds, StopwatchPauseVar
        PauseButton.config(text="Pause")
        StopwatchHours = 0
        StopwatchMinutes = 0
        StopwatchSeconds = -1
        StopwatchPauseVar = False
        counter()

    def pause():
        global StopwatchPauseVar
        StopwatchPauseVar = not StopwatchPauseVar
        if not StopwatchPauseVar:
            PauseButton.config(text="Pause")
        else:
            PauseButton.config(text="Resume")
        counter()

    def reset():
        global StopwatchHours, StopwatchMinutes, StopwatchSeconds, StopwatchPauseVar
        StopwatchPauseVar = True
        PauseButton.config(text="Pause")
        StopwatchHours = 0
        StopwatchMinutes = 0
        StopwatchSeconds = 0
        StopwatchTimerVar.set(f'{StopwatchHours:0>2}:{StopwatchMinutes:0>2}:{StopwatchSeconds:0>2}')
        StopwatchRoot.update()
        var.__del__()
        var["0,0"] = "Lap #"
        var["0,1"] = "Time"

    def lap():
        global StopwatchHours, StopwatchMinutes, StopwatchSeconds, RowCounter
        if RowCounter >= 6:
            var[f'1,0'] = var[f'2,0']
            var[f'2,0'] = var[f'3,0']
            var[f'3,0'] = var[f'4,0']
            var[f'4,0'] = var[f'5,0']
            var[f'1,1'] = var[f'2,1']
            var[f'2,1'] = var[f'3,1']
            var[f'3,1'] = var[f'4,1']
            var[f'4,1'] = var[f'5,1']
            var["5,0"] = RowCounter
            var["5,1"] = f'{StopwatchHours:0>2}:{StopwatchMinutes:0>2}:{StopwatchSeconds:0>2}'
        else:
            var[f'{RowCounter},0'] = RowCounter
            var[f'{RowCounter},1'] = f'{StopwatchHours:0>2}:{StopwatchMinutes:0>2}:{StopwatchSeconds:0>2}'
        RowCounter += 1
        root.update()

    def counter():
        global StopwatchHours, StopwatchMinutes, StopwatchSeconds, StopwatchPauseVar
        while not StopwatchPauseVar:
            StopwatchSeconds += 1
            if StopwatchMinutes == 60:
                StopwatchHours += 1
                StopwatchMinutes -= 60
            if StopwatchSeconds == 60:
                StopwatchSeconds -= 60
                StopwatchMinutes += 1
            StopwatchTimerVar.set(f'{StopwatchHours:0>2}:{StopwatchMinutes:0>2}:{StopwatchSeconds:0>2}')
            StopwatchRoot.update()
            time.sleep(1)
            counter()

    # Create widgets

    StopwatchRoot = Toplevel()
    StopwatchPopup = Frame(StopwatchRoot)

    var = TKTable.ArrayVar(StopwatchRoot)
    var["0,0"] = "Lap #"
    var["0,1"] = "Time"

    StopwatchPopup.grid(padx=25, pady=25)
    StopwatchTitleLabel = Label(StopwatchPopup, text="Stopwatch", font=("Futura", 36))
    StopwatchBorder = LabelFrame(StopwatchPopup)
    StopwatchTimerVar = StringVar()
    StopwatchTimerVar.set("00:00:00")
    StopwatchTimer = Label(StopwatchBorder, textvariable=StopwatchTimerVar, font=("Futura", 72))
    StartButton = Button(StopwatchPopup, text="Start", font=("Futura", 12), command=start)
    PauseButton = Button(StopwatchPopup, text="Pause", font=("Futura", 12), command=pause)
    ResetButton = Button(StopwatchPopup, text="Reset", font=("Futura", 12), command=reset)
    LapButton = Button(StopwatchPopup, text="Lap", font=("Futura", 12), command=lap)
    LapsTable = TKTable.Table(StopwatchPopup, rows=6, cols=2, variable=var, titlerows=1, roworigin=0, colorigin=0)

    StopwatchTitleLabel.grid(row=1, column=2, columnspan=2)
    StopwatchBorder.grid(row=2, column=1, columnspan=4)
    StopwatchTimer.grid(row=1)
    StartButton.grid(row=3, column=1)
    PauseButton.grid(row=3, column=2)
    ResetButton.grid(row=3, column=3)
    LapButton.grid(row=3, column=4)
    LapsTable.grid(row=4, column=2, columnspan=2)


def exitApp():
    sys.exit()


# MAIN
root = Tk()
mainframe = Frame(root)

DateCalcVar = False
TimerVar = False
StopwatchVar = False

# Create widgets
menubar = Menu(root)

DateCalculVar = BooleanVar()
DateCalcul = Menu(menubar, tearoff=0)
DateCalcul.add_command(label="Run", command=chooseDateCalc)
menubar.add_cascade(label="Date Calculator", menu=DateCalcul)

Timer = Menu(menubar, tearoff=0)
Timer.add_command(label="Run", command=chooseTime)
menubar.add_cascade(label="Timer", menu=Timer)

Stopwatch2 = Menu(menubar, tearoff=0)
Stopwatch2.add_command(label="Run", command=chooseStopwatch2)
menubar.add_cascade(label="Stopwatch", menu=Stopwatch2)

ExitMenu = Menu(menubar, tearoff=0)
ExitMenu.add_command(label="Exit", command=exitApp)
menubar.add_cascade(label="Exit the App", menu=ExitMenu)

Help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=Help)

WelcomeLabel = Label(mainframe, text="Welcome Time+ \n Please choose an application to use", font=("Futura", 16))
DateCalcButton = Button(mainframe, text="Date Calculator", command=chooseDateCalc)
TimerButton = Button(mainframe, text="Timer", command=chooseTime)
StopwatchButton = Button(mainframe, text="Stopwatch", command=chooseStopwatch2)
ExitApplicationButton = Button(mainframe, text="Exit the Application", command=exitApp)

# Grid widgets
root.title("Stopwatch/Timer/Date Calculator")
mainframe.grid(padx=50, pady=50)
root.minsize(width=300, height=100)

WelcomeLabel.grid(row=1, column=2, columnspan=2, sticky=EW)
DateCalcButton.grid(row=2, column=1, sticky=EW)
TimerButton.grid(row=2, column=2, sticky=EW)
StopwatchButton.grid(row=2, column=3, sticky=EW)
ExitApplicationButton.grid(row=2, column=4, sticky=EW)

root.config(menu=menubar)
root.mainloop()
