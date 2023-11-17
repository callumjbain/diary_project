from lib.diary_entry import *




def test_formatted_diary_entry():
    diaryentry = DiaryEntry("Day One", "This is my first entry into my diary.")
    result = diaryentry.format()
    assert result == "Day One: This is my first entry into my diary."

# return the nnunber of words in the diary entry. 
def test_number_of_words_in_diary_entry():
    diaryentry = DiaryEntry("Day One", "This is my first entry into my diary.")
    result = diaryentry.count_words()
    assert result == 8

# enter and int which represents words that can be read per minute
# returns estimated reading time as a result 

def test_reading_time_for_user():
    diaryentry = DiaryEntry("Day One", "This is my first entry into my diary.")
    result = diaryentry.reading_time(4)
    assert result == 2

def test_return_chunk_of_text():
    diaryentry = DiaryEntry("Day One", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt")

    result = diaryentry.reading_chunk(10, 10)
    assert result == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt"