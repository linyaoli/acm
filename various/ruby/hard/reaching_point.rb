# https://leetcode.com/problems/reaching-points/description/
# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} tx
# @param {Integer} ty
# @return {Boolean}
def reaching_points(sx, sy, tx, ty)
  while sx < tx && sy < ty
    tx, ty = tx % ty, ty % tx
  end

  return (sx == tx && (ty - sy) % sx == 0) || (sy == ty && (tx - sx) % sy == 0) 
end

#p reaching_points(1,1,2,2)
#p reaching_points(1,1,1,1)
#p reaching_points(1,1,3,5)
#p reaching_points(1,1,100000000,1)
p reaching_points(1,8,4,15)
