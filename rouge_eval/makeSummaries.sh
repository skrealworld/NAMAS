#!/bin/sh

MYFILE=$1
LENGTH=$2
REFERENCE=$3

#echo "summary algorithm: luhn"
#sumy luhn --length=$LENGTH --file=$MYFILE
#echo
#echo "evaluation"
#sumy_eval luhn $REFERENCE --length=$LENGTH --file=$MYFILE --format=plaintext
#echo
#echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#echo
#echo "summary algorithm: edmundson"
#sumy edmundson --length=$LENGTH --file=$MYFILE
#echo
#echo "evaluation"
#sumy_eval edmundson $REFERENCE --length=$LENGTH --file=$MYFILE --format=plaintext
#echo
#echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#echo
echo "summary algorithm: lsa"
sumy lsa --length=$LENGTH --file=$MYFILE
echo
echo "evaluation"
sumy_eval lsa $REFERENCE --length=$LENGTH --file=$MYFILE --format=plaintext
echo
#echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#echo
#echo "summary algorithm: text-rank"
#sumy text-rank --length=$LENGTH --file=$MYFILE
#echo
#echo "evaluation"
#sumy_eval text-rank $REFERENCE --length=$LENGTH --file=$MYFILE --format=plaintext
#echo
#echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#echo
#echo "summary algorithm: lex-rank"
#sumy lex-rank --length=$LENGTH --file=$MYFILE
#echo
#echo "evaluation"
#sumy_eval lex-rank $REFERENCE --length=$LENGTH --file=$MYFILE --format=plaintext
#echo
#echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#echo
#echo "summary algorithm: sum-basic"
#sumy sum-basic --length=$LENGTH --file=$MYFILE
#echo
#echo "evaluation"
#sumy_eval sum-basic $REFERENCE --length=$LENGTH --file=$MYFILE --format=plaintext
#echo
#echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#echo
#echo "summary algorithm: kl"
#sumy kl --length=$LENGTH --file=$MYFILE
#echo
#echo "evaluation"
#sumy_eval kl $REFERENCE --length=$LENGTH --file=$MYFILE --format=plaintext

#echo
#echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#echo
