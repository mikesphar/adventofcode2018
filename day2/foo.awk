#!/usr/bin/gawk -f
function similarchars(box, box2) {
  similar = ""
  split(box, b1, "")
  split(box2, b2, "")
  for (n in b1) {
    if (b1[n] == b2[n]) similar = similar b1[n]
  }
  return similar
}
{
  boxes[$i] = 1
}
END {
  for (box in boxes) {
    for (box2 in boxes) {
      similar = similarchars(box, box2)
      if (length(similar) == length(box) -1) {
        print similar
        exit
      }
    }
  }
}
