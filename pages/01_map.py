import solara
import leafmap.leafmap as leafmap

def create_split_map():
    split_control = leafmap.split_map(
        left_layer="Esri.WorldImagery",  # 左邊：衛星影像
        right_layer="OpenStreetMap",     # 右邊：街道圖
        left_label="衛星影像",
        right_label="街道地圖",
        center=[23.632, 121.380],  # 花蓮馬太鞍溪中心座標
        zoom=14,                    # 適合河段細節
    )

    # 調整地圖高度
    split_control.layout.height = "650px"

    return split_control

@solara.component
def Page():
    solara.Markdown("## 馬太鞍溪捲簾比對 (Split Map)")
    solara.Markdown(
        "使用滑動分割視窗比對衛星影像與街道地圖，觀察馬太鞍溪位置與附近河流地勢。"
    )

    # 使用 use_memo 產生地圖物件
    split_widget = solara.use_memo(create_split_map, dependencies=[])

    # 放在 Column 容器內顯示
    with solara.Column(style={"width": "100%", "height": "700px"}):
        solara.display(split_widget)