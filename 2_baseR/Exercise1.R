# Activity 1 - Simple sums
100*56/4
(4*12)/3
4e+2

help(sd)

#Activity 2
a <- c(1:200)
a
b <- a*123
b
b[44]
b_sub <- b[1:15]
b_sub
b_sub <- c(b_sub, 24108, 24231)
b_sub
c <- c('actb', 100, 3.4)
c_sub <- c[2]
c_sub/4
char <- c(animal = c("dog", "cat"), city = "Tokyo", city = "London", food = "treat", age = "12 yrs")
char[names(char) == "city"]
names(char)
attributes(char)
char_a <- c("animal" = "dog", "city" = "Tokyo", "food" = "treat", "age" = "12 yrs")
char_a
names(char_a)

#Activity 3
#Matrix
x <- matrix(1:9, nrow = 3)
x
x[2,3]
y <- matrix(1:12, nrow = 3, byrow = T)
y
colnames(y) <- c("First", "Second", "Third", "Fourth")
colnames(y)
rownames(y) <- c("row1", "row2", "row3")
y

#Array
myarray <- array(1:24, dim = c(4,2,3))
myarray
myarray[3,2,2]
last_matrix <- myarray[,,3]
last_matrix

#Lists
a <- list(myarray, 4, "Exercise", y, TRUE)
a
a[[3]]
a[[5]]
a[c(3,5)]
class(a)
class(myarray)
help("iris")

#Activity 4
#Dataframes
bed_file <- read.table("/project/obds/shared/resources/2_r/baseR/coding_gene_region.bed", header = F, sep = "\t")
head(bed_file)
summary(bed_file)
dim(bed_file)
class(bed_file)
nrow(bed_file)
ncol(bed_file)
colnames(bed_file) <- c("chr", "start", "stop", "name", "score", "strand")
head(bed_file)
colnames(bed_file)
names(bed_file)
bed_file[30,3]
start <- bed_file[,2]
col2 <- bed_file$start
bed_file$int_length <- bed_file$stop - bed_file$start
head(bed_file)
region_subset <- bed_file[bed_file$int_length > 100000 & bed_file$int_length <= 200000, ]
head(region_subset)
write.table(region_subset, "intervals_100kto200k.txt", sep = "\t", quote = F, row.names = F)
