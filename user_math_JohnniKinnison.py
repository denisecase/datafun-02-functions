"""Johnni Kinnison Module 2-8/31/23"""

import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def total_number_of_beats(beats_per_measure, measures):
    """This function returns the total number of beats per song
    given beats per measure and measures per song"""
    return (beats_per_measure * measures)
def total_number_of_sheets_of_music(sheets_for_Bach, sheets_for_Clementi):
    """This function returns the total number of sheets of music for two different pieces"""
    return (sheets_for_Bach + sheets_for_Clementi)
def average_tempo (number_of_beats_in_a_song, number_of_minutes_a_song_is):
    """This function returns the average tempo of a song given the number of beats in a song and the number of minutes a song is and round it up to the nearest whole number."""
    return math.ceil(number_of_beats_in_a_song / number_of_minutes_a_song_is)
def musicians_pay(hourly_rate, hours_worked):
    """This function returns the total musicians pay by multiplying the hourly rate and the hours worked by the musician."""
    return (hourly_rate * hours_worked)


logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

logger.info(f'total_number_of_beats(4, 20) = {total_number_of_beats(4,20)}')
logger.info(f'total_number_of_beats(6, 11) = {total_number_of_beats(6,11)}')
logger.info(f'total_number_of_beats(3, 15) = {total_number_of_beats(3,15)}')
logger.info(f'total_number_of_sheets_of_music(5, 10) = {total_number_of_sheets_of_music(5, 10)}')
logger.info(f'total_number_of_sheets_of_music(6, 11) = {total_number_of_sheets_of_music(6, 11)}')
logger.info(f'total_number_of_sheets_of_music(15, 20) = {total_number_of_sheets_of_music(15, 20)}')
logger.info(f'averag_tempo(139, 4.2) = {average_tempo(139, 4.2)}')
logger.info(f'averag_tempo(150, 3.5) = {average_tempo(150, 3.5)}')
logger.info(f'averag_tempo(120, 5.1) = {average_tempo(120, 5.1)}')
logger.info(f'musicians_pay(20.50, 6) = {musicians_pay(20.50, 6)}')
logger.info(f'musicians_pay(25.25, 10) = {musicians_pay(25.25, 10)}')
logger.info(f'musicians_pay(15.75, 8) = {musicians_pay(15.75, 8)}')