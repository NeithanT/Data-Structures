#ifndef LIST_HPP
#define LIST_HPP

template <typename T>

class SimpleList {

    struct SimpleNode {
        T data;
        SimpleNode* next;
        SimpleNode(const T& value) : data(value), next(nullptr) {}
    };
    SimpleNode* head;
    SimpleNode* tail;
    // Optional: to keep track of the size
    size_t list_size;

public:

    /**
     * 
     */
    void push_back(const T& value);
    
    /**
     * 
     */
    void pop_back();

    /**
     * 
     */
    T& back();

    /**
     * 
     */
    const T& back() const;

    /**
     * 
     */
    bool empty() const;

    /**
     * 
     */
    size_t size() const;

};

#endif // LIST_HPP