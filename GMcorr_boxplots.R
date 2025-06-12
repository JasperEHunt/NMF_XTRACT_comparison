# Load in data and transform data shape
NMFsurfcorrs = read.csv("/path/to/data/surf_compare.csv");
NMFsurfcorrs$K <- factor(NMFsurfcorrs$K , levels=c("10", "50", "60", "100", "200"));

# Generate box plot
boxplot(val~K,
        data=NMFsurfcorrs,
        main="Macaque: maximal correlations for different component numbers, surface space",
        xlab="Number of components (K)",
        ylab="Maximal correlation",
        ylim = c(0, 0.90),
        col="peachpuff1",
        border="peachpuff3",
        notch=TRUE,
        outline=FALSE,
        names=c("10", "50", "60", "100", "200"))

# Overlay data points
stripchart(val~K,
           data=NMFsurfcorrs,
           method="jitter",
           pch=21,
           col="peachpuff4",
           vertical=TRUE,
           lwd="2",
           add=TRUE)
