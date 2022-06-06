#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is not None:
        len_sent = len(sentence)
        if len_sent == 0:
            return (len_sent, None)
        return (len_sent, sentence[0])


if __name__ == '__main__':
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
