library(ggplot2)

#load Titanic Titanicing data for analysis. Open in spreadsheet view.
titanic <- read.csv("~/Pyton_Work/titanic.csv", stringsAsFactors = FALSE)

View(titanic)

#set up factors.
titanic$class <- as.factor(titanic$class)
titanic$survived <- as.factors(titanic$survived)
titanic$gender <- as.factor(titanic$gender)
titanic$embarked <- as.factor(titanic$embarked)

ggplot(titanic, aes(x = survived)) + geom_bar()

prop.table(table(titanic$survived))

ggplot(titanic, aes(x = survived)) + 
  theme_bw() + 
  geom_bar() +
  labs(y="Passenger Count",
       title="Titanic Survival Rates")

ggplot(titanic, aes(x = gender, fill = survived)) + 
  theme_bw() + 
  geom_bar() +
  labs(y="Passenger Count",
       title="Titanic Survival Rates by gender")
