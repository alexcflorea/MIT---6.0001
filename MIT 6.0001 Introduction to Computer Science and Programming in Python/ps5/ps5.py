# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Alex Florea
# Collaborators: None
# Time: 7-8 hours

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        '''
        Initializes a NewsStory object
                
        guid (string): A globally unique identifier for this news story
        title (string): The news story's headline
        description (string): A paragraph or so summarizing the news story
        link (string): A link to a website with the entire story
        pubdate (datetime): Date the news was published

        A SubMessage object has five attributes:
            self.guid (string)
            self.title (string)
            self.description (string)
            self.link (string)
            pubdate (datetime)
        '''
        
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        '''
        Used to safely access self.guid outside of the class
        
        Returns: self.guid
        '''
        return self.guid
    
    def get_title(self):
        '''
        Used to safely access self.title outside of the class
        
        Returns: self.title
        '''
        return self.title
    
    def get_description(self):
        '''
        Used to safely access self.description outside of the class
        
        Returns: self.description
        '''
        return self.description
    
    def get_link(self):
        '''
        Used to safely access self.link outside of the class
        
        Returns: self.link
        '''
        return self.link
    
    def get_pubdate(self):
        '''
        Used to safely access self.pubdate outside of the class
        
        Returns: self.pubdate
        '''
        return self.pubdate
    
    
    
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        """
        Initializes a PhraseTrigger object
        
        phrase (string): phrase used to fire trigger
        """
        
        self.phrase = phrase
        
    def is_phrase_in(self, text):
        """
        Used to test if entire phrase is present in text. Ignores punctuation
        
        Returns: True if whole phrase present
        """
        textNoPunct = text
        phraseNoPunct = self.phrase
        
        for char in string.punctuation:
            textNoPunct = textNoPunct.replace(char, ' ')
            phraseNoPunct = phraseNoPunct.replace(char, ' ')
       
        
        cleanPhrase = ' '.join(phraseNoPunct.lower().split()) + ' '
        cleanText = ' '.join(textNoPunct.lower().split()) + ' '
        
        return cleanPhrase in cleanText
    
        
    
# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for a phrase in the given title, or False otherwise.
        """
        return super().is_phrase_in(story.get_title())
    

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for a phrase in the given description, or False otherwise.
        """
        return super().is_phrase_in(story.get_description())
    
# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, strTime):
        """
        Input: strTime (string) has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        Convert time from string to a datetime before saving it as an attribute.
        """
        time = datetime.strptime(strTime, "%d %b %Y %H:%M:%S")
        time = time.replace(tzinfo=pytz.timezone("EST"))
        self.time = time
        
        
# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        """
        Returns True when a story is published strictly
        before the trigger’s time, or False otherwise.
        """
        return story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) < self.time



class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        """
        Returns True when a story is published strictly
        after the trigger’s time, or False otherwise.
        """
        return story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) > self.time
    
# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(object):
    def __init__(self, trigger):
        self.trigger = trigger
        
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
class AndTrigger(object):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
        
    def evaluate(self, story):
        return self.trig1.evaluate(story) and self.trig2.evaluate(story)

# Problem 9
class OrTrigger(object):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
        
    def evaluate(self, story):
        return self.trig1.evaluate(story) or self.trig2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filteredList = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filteredList.append(story)
                continue
            
    return filteredList
                



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    triggerdict = {}
    triggerlist = []
    for data in lines:
        data = data.split(',')
        if data[0] == 'ADD':
            triggerlist += (triggerdict[i] for i in data[1:])
            
        elif data[1] == 'AND' or data[1] == 'OR':
            triggerdict[data[0]] = trig_def(data[1], triggerdict[data[2]], triggerdict[data[3]])
            
        else:
            triggerdict[data[0]] = trig_def(data[1], data[2])
            
    return triggerlist
            

def trig_def(description, *args):
    if description == 'TITLE':
        trigName = TitleTrigger(args[0])
        
    elif description == 'DESCRIPTION':
        trigName = DescriptionTrigger(args[0])
        
    elif description == 'AFTER':
        trigName = AfterTrigger(args[0])
        
    elif description == 'BEFORE':
        trigName = BeforeTrigger(args[0])
        
    elif description == 'NOT':
        trigName = NotTrigger(args[0])
        
    elif description == 'AND':
        trigName = AndTrigger(args[0], args[1])
        
    elif description == 'OR':
        trigName = OrTrigger(args[0], args[1])
        
        
    return trigName

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('current_triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # Yahoo news doesn't seem to work well...
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':        
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()