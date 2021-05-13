{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8ec5681c-0535-443e-9eb9-22d589f1fcb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "315035a4-dcdb-4583-b9ce-e649f9d2ef3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "app= Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "acf76cdf-9611-46f4-aa9c-cde72dbc6876",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def hello_world():\n",
    "    return 'Hello World'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22db5879-4230-4eb3-865e-7a01090f669c",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
