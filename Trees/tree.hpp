#ifndef TREE_HPP
#define TREE_HPP

#include <iostream>

// Note that is is a basic tree, where it has a starting value and smaller values go
// left and bigger values go right
template <typename T>

/**
 * 
 */
class TreeNode {

public:

    T data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(T value) : data(value), left(nullptr), right(nullptr) {}
    TreeNode() : data(T()), left(nullptr), right(nullptr) {}
};


template <typename T>

/**
 * 
 */
class Tree {

private:

    TreeNode<T>* root;

    void insert(TreeNode<T>*& node, T value);

public:

    Tree() : root(nullptr) {}

    void insert(T value);

    void toString(TreeNode<T>* node);

    void display();

};

#endif // TREE_HPP