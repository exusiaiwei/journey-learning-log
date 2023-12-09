# 设置工作目录
#setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

# 加载所需的包
install.packages("ggplot2")  # 如果未安装ggplot2，则需要先安装
library(ggplot2)

# 读取数据文件
data <- read.csv("ll数据.csv")

# 使用ggplot函数创建折线图，并添加自定义主题
ggplot(data, aes(x = Time)) +
  geom_line(aes(y = Text, color = "Text"), size = 0.8) +
  geom_line(aes(y = Image, color = "Image"), size = 0.8) +
  labs(title = "Text and Image Fixations Over Time", x = "Time (milliseconds)", y = "Fixations", color = "Variable") +
  scale_color_brewer(palette = "Set2") +  # 使用Set2颜色主题
  theme_minimal(base_size = 16) +  # 调整整体字体大小为14pt
  theme(
    # 设置绘图区背景色为纯白色
    panel.background = element_rect(fill = "white"),
    # 设置主要网格线样式为虚线
    panel.grid.major = element_line(color = "gray", linetype = "dashed", size = 0.5),
    # 设置坐标轴标签大小和颜色，字体使用serif，距离坐标轴留出20pt的距离
    axis.text = element_text(size = 16, color = "black", family = "serif", margin = margin(20, 20, 0, 0, unit = "pt")),
    # 设置坐标轴标题大小和颜色，字体使用serif，距离坐标轴留出20pt的距离
    axis.title = element_text(size = 18, color = "black", family = "serif", margin = margin(20, 0, 20, 0, unit = "pt")),
    # 设置标题大小、加粗和居中，字体使用serif，距离图表留出40pt的距离
    plot.title = element_text(size = 24, face = "bold", hjust = 0.5, family = "serif", margin = margin(0, 0, 40, 0, unit = "pt")),
    # 将图例放置在右上角，留出边距
    legend.position = c(0.95, 0.95),
    legend.justification = c(1, 1),
    legend.margin = margin(5, 5, 5, 5, unit = "pt"),
    # 设置图例标题大小、加粗和颜色，字体使用serif
    legend.title = element_text(size = 16, face = "bold", color = "black", family = "serif"),
    # 设置图例标签大小和颜色，字体使用serif
    legend.text = element_text(size = 16, color = "black", family = "serif")
  ) +
  # 设置x轴和y轴的取值范围从0开始
  xlim(0, NA) +
  ylim(0, NA)