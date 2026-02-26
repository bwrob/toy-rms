#set page(width: 600pt, height: 120pt, margin: 10pt, fill: none)

#let risk-green = rgb("#239471")
#let dark-green = rgb("#1a6e54")
#let toy-yellow = rgb("#FFD700")

#let logo(size: 80pt) = {
  let scale-factor = size / 200pt
  box(
    width: size,
    height: size,
    fill: risk-green,
    radius: 15pt * scale-factor,
    stroke: (5pt * scale-factor) + dark-green,
    align(center + horizon)[
      #stack(
        dir: ttb,
        spacing: -15pt * scale-factor,
        [#set text(size: 100pt * scale-factor, fill: white, weight: "bold", font: "Libertinus Serif"); T],
        #align(center)[
          #stack(
            dir: ltr,
            spacing: 5pt * scale-factor,
            rect(width: 10pt * scale-factor, height: 15pt * scale-factor, fill: toy-yellow, radius: 2pt * scale-factor),
            rect(width: 10pt * scale-factor, height: 25pt * scale-factor, fill: toy-yellow, radius: 2pt * scale-factor),
            rect(width: 10pt * scale-factor, height: 10pt * scale-factor, fill: toy-yellow, radius: 2pt * scale-factor),
            rect(width: 10pt * scale-factor, height: 30pt * scale-factor, fill: toy-yellow, radius: 2pt * scale-factor),
          )
        ]
      )
    ]
  )
}

#align(horizon)[
  #stack(
    dir: ltr,
    spacing: 20pt,
    logo(size: 100pt),
    [
      #set text(size: 64pt, weight: "bold", font: "Liberation Sans")
      #text(fill: risk-green)[Toy]#text(fill: dark-green)[RMS]

      #v(-20pt)
      #line(length: 100%, stroke: (paint: toy-yellow, thickness: 3pt, dash: "dashed"))
    ]
  )
]
