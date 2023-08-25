{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4667367",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "09caaacd",
   "metadata": {},
   "source": [
    "## Visual Python Upgrade\n",
    "NOTE: \n",
    "- Refresh your web browser to start a new version.\n",
    "- Save VP Note before refreshing the page."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3d402f19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: visualpython in c:\\users\\hp\\anaconda3\\lib\\site-packages (2.4.7)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -cipy (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ensorflow-intel (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -cipy (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ensorflow-intel (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "\n",
      "[notice] A new release of pip is available: 23.1.2 -> 23.2.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "# Visual Python\n",
    "!pip install visualpython --upgrade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7dac5543",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Package install command: pip\n",
      "==========================================================================================\n",
      "Already exists Visual Python.\n",
      "==========================================================================================\n",
      "==========================================================================================\n",
      "Remove Visual Python Directories.\n",
      "==========================================================================================\n",
      "Copy visualpython extension files ...\n",
      "------------------------------------------------------------------------------------------\n",
      "Source Dir : c:\\users\\hp\\anaconda3\\lib\\site-packages\\visualpython\n",
      "Target Dir : C:\\Users\\HP\\anaconda3\\share\\jupyter\\nbextensions\\visualpython\n",
      "==========================================================================================\n",
      "551 File(s) copied\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Disabling notebook extension visualpython/visualpython...\n",
      "      - Validating: ok\n",
      "Enabling notebook extension visualpython/visualpython...\n",
      "      - Validating: ok\n"
     ]
    }
   ],
   "source": [
    "# Visual Python\n",
    "!visualpy install"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bf569ced",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyttsx3 in c:\\users\\hp\\anaconda3\\lib\\site-packages (2.90)\n",
      "Requirement already satisfied: comtypes in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pyttsx3) (1.1.10)\n",
      "Requirement already satisfied: pypiwin32 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pyttsx3) (223)\n",
      "Requirement already satisfied: pywin32 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pyttsx3) (302)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -cipy (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ensorflow-intel (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -cipy (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ensorflow-intel (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "\n",
      "[notice] A new release of pip is available: 23.1.2 -> 23.2.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install pyttsx3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3c7bad11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: SpeechRecognition in c:\\users\\hp\\anaconda3\\lib\\site-packages (3.10.0)\n",
      "Requirement already satisfied: requests>=2.26.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from SpeechRecognition) (2.28.1)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests>=2.26.0->SpeechRecognition) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests>=2.26.0->SpeechRecognition) (3.3)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests>=2.26.0->SpeechRecognition) (1.26.11)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests>=2.26.0->SpeechRecognition) (2022.9.14)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -cipy (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ensorflow-intel (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -cipy (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ensorflow-intel (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "\n",
      "[notice] A new release of pip is available: 23.1.2 -> 23.2.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install SpeechRecognition\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "136bdc7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyaudio in c:\\users\\hp\\anaconda3\\lib\\site-packages (0.2.13)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -cipy (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ensorflow-intel (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -cipy (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ensorflow-intel (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\users\\hp\\anaconda3\\lib\\site-packages)\n",
      "\n",
      "[notice] A new release of pip is available: 23.1.2 -> 23.2.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install pyaudio\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "74a22304",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyttsx3\n",
    "import speech_recognition as sr\n",
    "from time import ctime ,sleep\n",
    "import webbrowser\n",
    "import random\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d612083a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def voice(play_voice):\n",
    "    engine = pyttsx3.init()\n",
    "\n",
    "    voices = engine.getProperty('voices')\n",
    "    engine.setProperty('voice', voices[1].id)\n",
    "\n",
    "    rate = engine.getProperty('rate')\n",
    "    engine.setProperty('rate', rate - 60)\n",
    "\n",
    "    engine.say(play_voice)\n",
    "    engine.runAndWait()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "607c5b19",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_voice():\n",
    "\n",
    "    global voice_data\n",
    "    voice_data = \"\"\n",
    "\n",
    "    while True:\n",
    "        r = sr.Recognizer()\n",
    "        with sr.Microphone() as source:\n",
    "\n",
    "            try:\n",
    "                audio = r.listen(source)\n",
    "                voice_data = r.recognize_google(audio)\n",
    "                sleep(1)\n",
    "                break\n",
    "\n",
    "            except:\n",
    "                continue\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f18899d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_voice_2():\n",
    "\n",
    "    global voice_data2\n",
    "    voice_data2 = \"\"\n",
    "\n",
    "    while True:\n",
    "        r_2 = sr.Recognizer()\n",
    "        with sr.Microphone() as source:\n",
    "            try:\n",
    "                audio = r_2.listen(source)\n",
    "                voice_data2 = r_2.recognize_google(audio)\n",
    "                sleep(1)\n",
    "                break\n",
    "            except:\n",
    "\n",
    "                break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2e79c252",
   "metadata": {},
   "outputs": [],
   "source": [
    "def greeting():\n",
    "    g_messages = [\"hi there.\",\"hey Akash.\",\"yeah im here.\",\"How can I help you Akash\",\"yes im here.\"]\n",
    "    r_message = random.choice(g_messages)\n",
    "    voice(r_message)\n",
    "\n",
    "def thanking():\n",
    "    th_messages = [\"you are welcome.\",\"its pleasure to being with you.\",\"Never mind its my job\"]\n",
    "    r_th_message = random.choice(th_messages)\n",
    "    voice(r_th_message)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8a71377a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_ip_info():\n",
    "\n",
    "    global internet_status\n",
    "    internet_status = False\n",
    "\n",
    "    try:\n",
    "        r = requests.get('https://get.geojs.io/')\n",
    "        ip_req = requests.get('https://get.geojs.io/v1/ip.json')\n",
    "        ip_add = ip_req.json()['ip']\n",
    "        # print(ip_add)\n",
    "\n",
    "        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'\n",
    "        geo_req = requests.get(url)\n",
    "        geo_data = geo_req.json()\n",
    "\n",
    "        global get_city , get_region , get_country\n",
    "\n",
    "        get_city = str((geo_data['city']))\n",
    "        get_region = str((geo_data['region']))\n",
    "        get_country = str((geo_data['country']))\n",
    "\n",
    "        internet_status = True\n",
    "\n",
    "    except:\n",
    "        internet_status = False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8d1d578",
   "metadata": {},
   "outputs": [],
   "source": [
    "def analyse_voice():\n",
    "\n",
    "    get_ip_info()\n",
    "\n",
    "    if internet_status == False:\n",
    "        voice(\"Check Your Internet Connection !\")\n",
    "        exit()\n",
    "\n",
    "    else:\n",
    "\n",
    "        voice(\"im Alexa How Can I Help You ?\")\n",
    "        joke_count = 0\n",
    "        answer_count = 0\n",
    "\n",
    "        while True:\n",
    "\n",
    "            if answer_count >= 5:\n",
    "                joke_count = 0\n",
    "                answer_count = 0\n",
    "\n",
    "            else:\n",
    "                pass\n",
    "\n",
    "            get_voice()\n",
    "            words = [\"time\",\"location\",\"city\",\"country\",\"hi\",\"hey\",\"bye\",\"thanks\",\n",
    "                     \"search\",\"town\",\"do\",\"old\",\"joke\",\"ok\",\"okay\",\"thank\",\"great\",\"wow\",\n",
    "                     \"name\",\"yoo\",\"yo\",\"tired\",\"sleep\",\"sleepy\",\"cool\",\"region\"]\n",
    "            x = str(voice_data)\n",
    "            z = x.split()\n",
    "            avl_words = 0\n",
    "\n",
    "            for y in z:\n",
    "                if y.lower() in words:\n",
    "                    avl_words += 1\n",
    "\n",
    "            if avl_words == 0:\n",
    "                print(x)\n",
    "                voice(\"Did Not Get you.\")\n",
    "                continue\n",
    "\n",
    "            elif avl_words >= 2:\n",
    "                voice(\"Cant Identify What You Actually Need ! speak again.\")\n",
    "                continue\n",
    "\n",
    "            else:\n",
    "                if \"Bye\" in z:\n",
    "                    voice(\"Good Bye Akash.\")\n",
    "                    break\n",
    "\n",
    "                else:\n",
    "                    for i in z:\n",
    "                        if i.lower() in words :\n",
    "\n",
    "                            if  joke_count >= 1:\n",
    "                                answer_count += 1\n",
    "\n",
    "                            else:\n",
    "                                pass\n",
    "\n",
    "                            if i.lower() ==\"time\":\n",
    "                                now_time = \"Now Time Is \" + ctime()\n",
    "                                converted_now_time = str(now_time)\n",
    "                                voice(converted_now_time)\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"town\":\n",
    "                                voice(\"Location is moratuwa.\")\n",
    "                                break\n",
    "\n",
    "                            elif i==\"city\":\n",
    "                                your_city = 'Your city Is,' + get_city + '.'\n",
    "                                voice(your_city)\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"hi\" or i.lower()==\"yoo\" or i.lower()==\"yo\" or i.lower()==\"hey\":\n",
    "                                greeting()\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"thanks\" or i.lower()==\"thank\":\n",
    "                                thanking()\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"search\":\n",
    "                                voice(\"What Do You Want To search.\")\n",
    "                                get_voice_2()\n",
    "\n",
    "                                if voice_data2 == \"\":\n",
    "                                    voice(\"Did Not Able To Find.\")\n",
    "                                    break\n",
    "                                else:\n",
    "\n",
    "                                    google_url = 'https://google.com/search?q=' + voice_data2\n",
    "                                    webbrowser.get().open(google_url)\n",
    "                                    voice(\"here what i got.\")\n",
    "                                    voice_data2 = \"\"\n",
    "                                    break\n",
    "                                    sleep(1.5)\n",
    "\n",
    "\n",
    "                            elif i.lower()==\"location\":\n",
    "                                voice(\"Where Do You Want To search.\")\n",
    "                                get_voice_2()\n",
    "\n",
    "                                if voice_data2 == \"\":\n",
    "                                    voice(\"Did Not Able To Find.\")\n",
    "                                    break\n",
    "                                else:\n",
    "                                    location_url = 'https://google.nl/maps/place/' + voice_data2 + '/&amp'\n",
    "                                    webbrowser.get().open(location_url)\n",
    "                                    voice(\"here what i got.\")\n",
    "\n",
    "                                    sleep(1.5)\n",
    "                                    voice_data2 = \"\"\n",
    "                                    break\n",
    "\n",
    "\n",
    "                            elif i.lower()==\"country\":\n",
    "                                your_country = 'Your country Is ,' + get_country + '.'\n",
    "                                voice(your_country)\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"region\":\n",
    "                                your_region = 'Your region Is ,' + get_region + '.'\n",
    "                                voice(your_region)\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"old\":\n",
    "\n",
    "                                voice(\"I have no idea about that. ask from the inventer.\")\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"do\":\n",
    "\n",
    "                                voice(\"I can do several thing for you as for now. in near future i will be upgraded with more. for now i can search what ever you want from google , find loactions , time , city , country & make you mood good Thats all.\")\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"joke\":\n",
    "\n",
    "                                if joke_count == 0:\n",
    "                                    voice(\"imagine, that how there is no internet connection in the world\")\n",
    "                                    joke_count += 1\n",
    "\n",
    "                                else:\n",
    "                                    voice(\"Im fed up with telling stories to you. so plz.\")\n",
    "                                break\n",
    "\n",
    "\n",
    "                            elif i.lower()==\"ok\" or i.lower()==\"okay\":\n",
    "\n",
    "                                voice(\"Sounds Good.\")\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"wow\" or i.lower()==\"great\" or i.lower()==\"cool\":\n",
    "\n",
    "                                voice(\"Its awesome being able to help.\")\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"name\":\n",
    "\n",
    "                                voice(\"my name is alexa.\")\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"tired\":\n",
    "\n",
    "                                voice(\"okay Akash take a rest.\")\n",
    "                                break\n",
    "\n",
    "                            elif i.lower()==\"sleep\" or i.lower()==\"sleepy\":\n",
    "\n",
    "                                voice(\"okay Akash go to the bed.\")\n",
    "                                break\n",
    "\n",
    "                        else:\n",
    "                            continue\n",
    "\n",
    "\n",
    "analyse_voice()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3971e431",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "vp": {
   "vp_config_version": "1.0.0",
   "vp_menu_width": 273,
   "vp_note_display": false,
   "vp_note_width": 0,
   "vp_position": {
    "width": 278
   },
   "vp_section_display": false,
   "vp_signature": "VisualPython"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
