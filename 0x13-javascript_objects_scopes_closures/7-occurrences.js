#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (list.length > 0 && searchElement) {
    let nocur = 0;
    for (let con = 0; con < list.length; con++) {
      if (list[con] === searchElement) {
        nocur = nocur + 1;
      }
    }
    return (nocur);
  }
};
