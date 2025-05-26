def get_grid_position(index,grid_width):
    return divmod(index, grid_width)
print(get_grid_position(17,5))
#output (3,2)