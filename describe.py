import pandas as pd
import sys
import nltk

def main():
	infile = '../Data/reviews_clean.csv'
    outfile = '../Output/describe.txt'
	df = pd.read_csv(infile)

    orig_stdout = sys.stdout
    f = file(outfile, 'w')
    sys.stdout = f

	describe(df)
    describe_nlp(df['text'])

    sys.stdout = orig_stdout
    f.close()

def describe(df):
    pd.options.display.max_colwidth = 1000

    df['date'].dt.year.value_counts()

    df[:2]
    df.columns.unique()
    [c for c in df.columns if 'business' in c]

def describe_nlp(col):
    text = col.to_string()
    text = text.lower()
    tokens = nltk.word_tokenize(text)

    # Lemmatization looks up words in a dictionary and changes to their root word
    wnl = nltk.WordNetLemmatizer()
    tokens = [wnl.lemmatize(t) for t in tokens]
    text = nltk.Text(tokens)

    print "Display all chunks with word 'mexican'\n"
    print text.concordance('mexican')
    print '\n'

    print "Display words that appear in a similar range of contexts as 'mexican'\n"
    print text.similar('mexican')
    print '\n'

    print "Display the contexts shared by 'mexican' and 'good'\n"
    text.common_contexts(['mexican', 'good'])
    print '\n'

    print "Word frequency\n"
    nltk.FreqDist(text)
    print '\n'

if __name__ == "__main__":
	main()