from typing import List, Any



def manual_deep_copy(list_3d: List) -> List[Any]:
    level1_copy = []
    for l1 in list_3d:
        level2_copy = []
        for l2 in l1:
            level3_copy = []
            for l3 in l2:
                if isinstance(l3, dict):
                    level3_copy.append(l3.copy())
                elif isinstance(l3, list):
                    level3_copy.append(l3[:])
                else:
                    level3_copy.append(l3)

            level2_copy.append(level3_copy)
        level1_copy.append(level2_copy)
    return level1_copy


original_data = [
        # Team 1
        [
            ['Player A', {'score': 10, 'fouls': 2}],
            ['Player B', {'score': 15, 'fouls': 1}]
        ],
        # Team 2
        [
            ['Player C', {'score': 7, 'fouls': 4}],
            ['Player D', {'score': 12, 'fouls': 0}]
        ]
    ]

