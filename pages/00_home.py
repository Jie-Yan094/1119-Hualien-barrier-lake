import solara

@solara.component
def Page():
    # 設定瀏覽器標籤頁的標題
    solara.Title("我的 Solara WebGIS App")
    solara.Markdown("### **花蓮馬太鞍溪堰塞湖 WebGIS 應用程式**")
    solara.Markdown("""
    這是一個使用 Solara 框架開發的 WebGIS 應用程式，展示了花蓮馬太鞍溪堰塞湖的地理資訊。
    """)
    solara.Image("https://example.com/hualien_barrier_lake_image.jpg", alt="花蓮堰塞湖圖片", width="600px")

