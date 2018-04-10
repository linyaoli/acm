# https://leetcode.com/problems/all-paths-from-source-to-target/description/
# @param {Integer[][]} graph
# @return {Integer[][]}
def all_paths_source_target(graph)
  @graph = graph
  @sol = []
  @res = []

  gen(0)
  return @res
end

def gen(i)
  if i == @graph.size - 1
    @res << [0, @sol[0..-1]].flatten
  else
    for j in 0..@graph[i].size-1
      if @graph[i][j] > i
        @sol << @graph[i][j]
        gen(@graph[i][j])
        @sol.pop
      end
    end
  end
end

p all_paths_source_target([[1,2], [3], [4], [3, 4], []])
