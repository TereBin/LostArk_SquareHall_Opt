import tkinter as tk
from tkinter import ttk

import heapq

graph = {"루테란": {"토토이크": 1100, "애니츠": 2000, "아르데타인": 3400, "베른 북부": 2100, "슈샤이어": 5000, "로헨델": 7100, "욘": 10000, "페이튼": 11000, "파푸니카": 7600, "베른 남부": 5000, "로웬": 9600, "엘가시아": 0, "플레체": 3200, "볼다이크": 7900, "쿠르잔 남부": 6000},
         "토토이크": {"루테란": 1100, "애니츠": 1100, "아르데타인": 2500, "베른 북부": 1900, "슈샤이어": 4600, "로헨델": 8000, "욘": 12000, "페이튼": 12000, "파푸니카": 9300, "베른 남부": 6100, "로웬": 9300, "엘가시아": 0, "플레체": 2200, "볼다이크": 9900, "쿠르잔 남부": 4200},
         "애니츠": {"루테란": 2000, "토토이크": 1100, "아르데타인": 1600, "베른 북부": 2000, "슈샤이어": 4200, "로헨델": 8800, "욘": 13000, "페이튼": 13000, "파푸니카": 11000, "베른 남부": 6900, "로웬": 8900, "엘가시아": 0, "플레체": 1700, "볼다이크": 12000, "쿠르잔 남부": 2700},
         "아르데타인": {"루테란": 3400, "토토이크": 2500, "애니츠": 1600, "베른 북부": 2100, "슈샤이어": 2900, "로헨델": 8900, "욘": 14000, "페이튼": 12000, "파푸니카": 12000, "베른 남부": 7000, "로웬": 7000, "엘가시아": 0, "플레체": 2400, "볼다이크": 14000, "쿠르잔 남부": 2500},
         "베른 북부": {"루테란": 2100, "토토이크":1900, "애니츠": 2000, "아르데타인": 2100, "슈샤이어": 2600, "로헨델": 5700, "욘": 9500, "페이튼": 8400, "파푸니카": 7600, "베른 남부": 3000, "로웬": 5600, "엘가시아": 0, "플레체": 1900, "볼다이크": 9000, "쿠르잔 남부": 5400},
         "슈샤이어": {"루테란": 5000, "토토이크": 4600, "애니츠": 4200, "아르데타인": 2900, "베른 북부": 2600, "로헨델":6000, "욘": 11000, "페이튼": 6800, "파푸니카": 10000, "베른 남부": 4800, "로웬": 2100, "엘가시아": 0, "플레체": 5200, "볼다이크": 13000, "쿠르잔 남부": 7600},
         "로헨델": {"루테란": 8600, "토토이크": 9700, "애니츠": 11000, "아르데타인": 11000, "베른 북부": 7000, "슈샤이어": 7300, "욘": 4400, "페이튼": 4100, "파푸니카": 4900, "베른 남부": 5500, "로웬": 9700, "엘가시아": 0, "플레체": 14000, "볼다이크": 8000, "쿠르잔 남부": 22000},
         "욘": {"루테란": 13000, "토토이크": 15000, "애니츠": 17000, "아르데타인": 18000, "베른 북부": 13000, "슈샤이어": 14000, "로헨델":4900, "페이튼": 10000, "파푸니카":6100, "베른 남부":13000, "로웬": 20000, "엘가시아": 0, "플레체": 25000, "볼다이크": 7800, "쿠르잔 남부":35000},
         "페이튼": {"루테란": 17000, "토토이크": 18000, "애니츠": 19000, "아르데타인": 18000, "베른 북부": 13000, "슈샤이어": 10000, "로헨델": 5200, "욘": 12000, "파푸니카": 15000, "베른 남부": 12000, "로웬": 12000, "엘가시아": 0, "플레체": 26000, "볼다이크": 21000, "쿠르잔 남부": 37000},
         "파푸니카": {"루테란": 12000, "토토이크": 15000, "애니츠": 18000, "아르데타인": 20000, "베른 북부": 12000, "슈샤이어": 17000, "로헨델": 6500, "욘": 7400, "페이튼": 16000, "베른 남부": 12000, "로웬": 25000, "엘가시아": 0, "플레체": 25000, "볼다이크": 5500, "쿠르잔 남부": 38000},
         "베른 남부": {"루테란": 5900, "토토이크": 9900, "애니츠": 11000, "아르데타인": 11000, "베른 북부": 3000, "슈샤이어": 7700, "로헨델": 7300, "욘": 16000, "페이튼": 13000, "파푸니카": 12000, "로웬": 12000, "엘가시아": 0, "플레체": 14000, "볼다이크": 17000, "쿠르잔 남부": 25000},
         "로웬": {"루테란": 15000, "토토이크": 15000, "애니츠": 14000, "아르데타인": 11000, "베른 북부": 9100, "슈샤이어": 3400, "로헨델": 13000, "욘": 24000, "페이튼": 13000, "파푸니카": 25000, "베른 남부": 12000, "엘가시아": 0, "플레체": 18000, "볼다이크": 32000, "쿠르잔 남부": 26000},
         "엘가시아": {"파푸니카":0},
         "플레체": {"루테란": 5200, "토토이크": 3500, "애니츠": 2800, "아르데타인": 3800, "베른 북부": 3000, "슈샤이어": 8300, "로헨델": 19000, "욘": 30000, "페이튼": 28000, "파푸니카": 25000, "베른 남부": 14000, "로웬": 18000, "엘가시아": 0, "볼다이크": 28000, "쿠르잔 남부": 9400},
         "볼다이크": {"루테란": 13000, "토토이크": 16000, "애니츠": 19000, "아르데타인": 22000, "베른 북부": 15000, "슈샤이어": 20000, "로헨델": 11000, "욘": 9400, "페이튼": 22000, "파푸니카": 5500, "베른 남부": 17000, "로웬": 31000, "엘가시아": 0, "플레체": 28000, "쿠르잔 남부": 41000},
         "쿠르잔 남부": {"루테란": 9700, "토토이크": 6900, "애니츠": 4300, "아르데타인": 4000, "베른 북부": 8600, "슈샤이어": 12000, "로헨델": 29000, "욘": 42000, "페이튼": 39000, "파푸니카": 38000, "베른 남부": 25000, "로웬": 26000, "엘가시아": 0, "플레체": 9400, "볼다이크": 41000}
         }

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous_vertices = {vertex: None for vertex in graph}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_vertices

def shortest_path(graph, start, end):
    distances, previous_vertices = dijkstra(graph, start)
    path = []
    current_vertex = end
    shortest_distance = distances[end]

    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]

    return path, shortest_distance

def cal():
    start = start_dd.get()
    end = end_dd.get()

    shortest_path_result, shortest_distance = shortest_path(graph, start, end)
    if start == end:
        straight_txt.set("직행 경로 : " + start + "\n비용 : 0")
        best_txt.set("최적 경로 : " + start + "\n비용 : 0")
    else:
        straight_txt.set("직행경로 : " + start + " - " + end + "\n비용 : " + str(graph.get(start).get(end)))
        best_txt.set("최적 경로 : " + ' - '.join(shortest_path_result) + "\n비용 : " + str(shortest_distance))

window = tk.Tk()
window.geometry("400x300+100+100")
window.resizable(False, False)
window.title("정기선 루트 계산기")

start_frame = tk.Frame(window, relief="solid", bd=1, padx=10, pady=10)
start_frame.place(x=10, y=10)
start_txt = tk.StringVar()
start_txt.set("출발지")
start_display = tk.Label(start_frame, textvariable=start_txt, width=50)
start_display.pack()
start_dd = ttk.Combobox(start_frame, state="readonly", values=["루테란", "토토이크", "애니츠", "아르데타인", "베른 북부", "슈샤이어", "로헨델", "욘", "페이튼", "파푸니카", "베른 남부", "로웬", "엘가시아", "플레체", "볼다이크", "쿠르잔 남부"])
start_dd.set("출발지를 선택해주세요")
start_dd.pack()

end_frame = tk.Frame(window, relief="solid", bd=1, padx=10, pady=10)
end_frame.place(x=10, y=90)
end_txt = tk.StringVar()
end_txt.set("목적지")
end_display = tk.Label(end_frame, textvariable=end_txt, width=50)
end_display.pack()
end_dd = ttk.Combobox(end_frame, state="readonly", values=["루테란", "토토이크", "애니츠", "아르데타인", "베른 북부", "슈샤이어", "로헨델", "욘", "페이튼", "파푸니카", "베른 남부", "로웬", "엘가시아", "플레체", "볼다이크", "쿠르잔 남부"])
end_dd.set("목적지를 선택해주세요")
end_dd.pack()

result_button = tk.Button(window, text="계산하기", command=cal)
result_button.place(x=10, y=160)

result_frame = tk.Frame(window, relief="solid", bd=1, padx=10, pady=5)
result_frame.place(x=10, y=190)

straight_txt = tk.StringVar()
straight_txt.set("직행 경로 : \n비용 : ")
straight_display = tk.Label(result_frame, textvariable=straight_txt, anchor="w", justify="left", width=50)
straight_display.pack()

best_txt = tk.StringVar()
best_txt.set("최적 경로 : \n비용 : ")
best_display = tk.Label(result_frame, textvariable=best_txt, anchor="w", justify="left", width=50)
best_display.pack()

sign_frm = tk.Frame(window)
sign_frm.place(x=10, y=275)
sign_txt = tk.StringVar()
sign_txt.set("LanceTereBin @아브렐슈드")
sign_display = tk.Label(sign_frm, textvariable=sign_txt, anchor="w", justify="left", width=50)
sign_display.pack()

window.mainloop()
