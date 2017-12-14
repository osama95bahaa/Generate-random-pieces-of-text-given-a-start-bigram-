{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 319,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import nltk\n",
    "from nltk import bigrams, trigrams\n",
    "from nltk import word_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "import string\n",
    "\n",
    "bigramsDict = {} \n",
    "trigramsDict = {}\n",
    "\n",
    "stop = set(stopwords.words('english'))\n",
    "punct = set(string.punctuation)\n",
    "\n",
    "for root, dirs, files in os.walk(r'single-docs'):\n",
    "    for file in (files[:10000]):\n",
    "        with open(os.path.join(root,file), 'r') as f:\n",
    "            \n",
    "            doc_words1 = word_tokenize(f.read().lower())\n",
    "            doc_words = [ word for word in doc_words1 if word not in stop] #Remove stopwords\n",
    "            doc_words = [''.join(word for word in doc_words if word not in punct) for doc_words in doc_words] # Remove Punct\n",
    "            doc_words = [word for word in doc_words if word] #Remove empty string\n",
    "            \n",
    "            doc_bigrams = set(list(bigrams(doc_words)))\n",
    "            doc_trigrams = set(list(trigrams(doc_words)))\n",
    "            \n",
    "            for d in doc_bigrams:    \n",
    "                if d not in bigramsDict:\n",
    "                    bigramsDict[d] = 1 \n",
    "                bigramsDict[d] = bigramsDict[d] +1\n",
    "            for d in doc_trigrams:    \n",
    "                if d not in trigramsDict:\n",
    "                    trigramsDict[d] = 1 \n",
    "                trigramsDict[d] = trigramsDict[d] +1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "836539\n"
     ]
    }
   ],
   "source": [
    "#Calculating the probability\n",
    "\n",
    "probabilityDict = {}\n",
    "\n",
    "for key,value in trigramsDict.items():\n",
    "    if(tuple([key[0], key[1]]) in bigramsDict.keys()):\n",
    "        probabilityDict[key] = value/bigramsDict[tuple([key[0], key[1]])]\n",
    "        \n",
    "print(len(probabilityDict))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 321,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('states', 'army', 'wanted', 'become', 'soldier', 'guthrie', 'went', 'physical', 'examination', 'doctor', 'fill', 'questionnaire', 'giving', 'information', 'areas', 'near', 'east', 'agriculture')\n"
     ]
    }
   ],
   "source": [
    "#Generating random sentences\n",
    "\n",
    "sentence = ('states','army')\n",
    "\n",
    "length=20\n",
    "while(length >= 0):\n",
    "    for key, value in probabilityDict.items():\n",
    "        if(length>=0):\n",
    "            if(sentence[-2:] == tuple([key[0], key[1]])):\n",
    "                if(value >=0.05):\n",
    "                    sentence = sentence +(key[2],)\n",
    "                    length -= 1\n",
    "    length -= 1            \n",
    "\n",
    "print(sentence)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
