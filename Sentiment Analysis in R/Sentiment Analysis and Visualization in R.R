# Load necessary libraries for text analysis and visualization
library(janeaustenr)
library(stringr)
library(tidytext)
library(dplyr)

# Preparing the data from Jane Austen's books
tidy_data <- austen_books() %>%
  group_by(book) %>%
  mutate(
    linenumber = row_number(), 
    chapter = cumsum(str_detect(text, regex("\\bchapter\\b", ignore_case = TRUE)))
  ) %>%
  ungroup() %>%
  unnest_tokens(word, text)

# Filtering for positive sentiments from the Bing lexicon
positive_senti <- get_sentiments("bing") %>%
  filter(sentiment == "positive")

# Counting words with positive sentiment in the book "Emma"
tidy_data %>%
  filter(book == "Emma") %>%
  semi_join(positive_senti) %>%
  count(word, sort = TRUE)

# Install and load the tidyr package for data tidying
if (!requireNamespace("tidyr", quietly = TRUE)) {
  install.packages("tidyr")
}
library(tidyr)

# Extracting sentiments using the Bing lexicon
bing <- get_sentiments("bing")

# Analyzing sentiment for "Emma" by sections of 80 lines
Emma_sentiment <- tidy_data %>%
  inner_join(bing) %>%
  count(book = "Emma", index = linenumber %/% 80, sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(sentiment = positive - negative)

# Install and load the ggplot2 package for visualization
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}
library(ggplot2)

# Plotting sentiment across sections of "Emma"
ggplot(Emma_sentiment, aes(index, sentiment, fill = book)) +
  geom_bar(stat = "identity", show.legend = TRUE) +
  facet_wrap(~book, ncol = 2, scales = "free_x")

# Counting words by sentiment
counting_words <- tidy_data %>%
  inner_join(bing) %>%
  count(word, sentiment, sort = TRUE)

# Viewing the first few rows of the counting_words dataframe
head(counting_words)

# Visualizing high-frequency words by sentiment
counting_words %>%
  filter(n > 150) %>%
  mutate(n = ifelse(sentiment == "negative", -n, n)) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n, fill = sentiment)) +
  geom_col() +
  coord_flip() +
  labs(y = "Sentiment Score")

# Install and load packages for word cloud visualization
if (!requireNamespace("reshape2", quietly = TRUE)) {
  install.packages("reshape2")
}
if (!requireNamespace("wordcloud", quietly = TRUE)) {
  install.packages("wordcloud")
}
library(reshape2)
library(wordcloud)

# Creating a word cloud of sentiment terms
tidy_data %>%
  inner_join(bing) %>%
  count(word, sentiment, sort = TRUE) %>%
  acast(word ~ sentiment, value.var = "n", fill = 0) %>%
  comparison.cloud(colors = c("red", "dark green"), max.words = 100)
