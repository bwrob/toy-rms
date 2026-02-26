#set page(width: 200pt, height: 200pt, margin: 0pt)
#set text(font: "Libertinus Serif", weight: "bold", size: 100pt, fill: white)

#box(
  width: 100%,
  height: 100%,
  fill: rgb("#239471"), // Risk Green
  radius: 20pt,
  stroke: 5pt + rgb("#1a6e54"),
  align(center + horizon)[
    #stack(
      dir: ttb,
      spacing: -20pt,
      [T],
      #align(center)[
        #set text(size: 20pt)
        #stack(
          dir: ltr,
          spacing: 5pt,
          rect(width: 10pt, height: 15pt, fill: yellow, radius: 2pt),
          rect(width: 10pt, height: 25pt, fill: yellow, radius: 2pt),
          rect(width: 10pt, height: 10pt, fill: yellow, radius: 2pt),
          rect(width: 10pt, height: 30pt, fill: yellow, radius: 2pt),
        )
      ]
    )
  ]
)
