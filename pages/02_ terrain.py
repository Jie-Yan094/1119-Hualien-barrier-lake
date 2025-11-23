import solara
import leafmap.maplibregl as leafmap
import os

# 從 Hugging Face Secret 讀取 API Key
MAPTILER_KEY = os.environ.get("MAPTILER_API_KEY", "")

def create_3d_map():

    # 如果沒有 API Key，回傳基礎地圖
    if not MAPTILER_KEY:
        m = leafmap.Map(
            center=[23.632, 121.380],  # 馬太鞍溪中心
            zoom=14,
            style="OpenStreetMap",
        )
        m.layout.height = "700px"
        return m

    # MapTiler Outdoor-v2 具備 3D 地形
    style_url = f"https://api.maptiler.com/maps/outdoor-v2/style.json?key={MAPTILER_KEY}"

    m = leafmap.Map(
        style=style_url,
        center=[121.380,23.632],  # 馬太鞍溪河道
        zoom=14,
        pitch=60,     # 3D 傾斜
        bearing=20,   # 旋轉角度
    )
    m.layout.height = "700px"
    return m

@solara.component
def Page():

    if not MAPTILER_KEY:
        solara.Warning(
            "MapTiler API Key 未設定。請在 Hugging Face Space Settings 加入 'MAPTILER_API_KEY' Secret。"
        )

    # 🌏 新標題
    solara.Markdown("## 🌏 馬太鞍溪災害 3D 地形展示")

    # 快取地圖
    map_object = solara.use_memo(create_3d_map, dependencies=[MAPTILER_KEY])

    # Solara 需要用 to_solara() 才能顯示 maplibregl Map
    return map_object.to_solara()