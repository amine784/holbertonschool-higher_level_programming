#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let l = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      l += 1;
    }
  }
  return (l);
};
