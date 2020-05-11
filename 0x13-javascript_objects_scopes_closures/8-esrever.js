#!/usr/bin/node
exports.esrever = function (list) {
  const l = [];
  const len = list.length;
  let i = len - 1;
  for (i = len; i >= 0; i--) {
    l.push(list[i]);
  }
  return (l);
};
