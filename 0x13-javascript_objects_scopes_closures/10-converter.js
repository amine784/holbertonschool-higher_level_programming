#!/usr/bin/node
exports.converter = function (base) {
  function conv (data) { return (data.toString(base)); }
  return (conv);
};
