library(igraph)
net_file_location = as.character(readline("input net file name: "))
raw_data = read.table(net_file_location, sep = "\t", comment.char = "~")
if( is.na(raw_data[,c("V1")][1]))
{
  edgelist_data = raw_data[c("V2","V3")]
} else {
  edgelist_data = raw_data[c("V1","V2")]
}
# edgelist_data = raw_data[c("V1","V2")]
g <- graph.data.frame(edgelist_data)
# node_file_location = as.character(readline("input node file name: "))
# node_data = read.table(node_file_location)
# V(g)$x <- t(as.vector(node_data["V2"]))
# V(g)$y <- t(as.vector(node_data["V4"]))

V(g)$id = V(g)$name

# for(i in 1:vcount(g))
# {
#   V(g)[i]$id = V(g)[i]$name
# }

write.graph(g,gsub('.tntp','.net',net_file_location),format = c("pajek"))

write.graph(g,gsub('.tntp','.edges',net_file_location),format = c("edgelist"))