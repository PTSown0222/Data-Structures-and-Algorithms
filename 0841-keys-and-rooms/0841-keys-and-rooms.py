class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # graph connections - index is u and rooms_arr is v
        n = len(rooms)
        start_node = 0
        visited = set([start_node])
        stack = [start_node]

        while stack:
            current_room = stack.pop()

            for key in rooms[current_room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
        
        return len(visited) == len(rooms)

        
        