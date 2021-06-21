package models

import "time"

// User is struct
type User struct {
	Login   string `json:"login"`
	ID      uint64 `json:"id"`
	HTMLURL string `json:"html_url"`
	Type    string `json:"type"`
}

//IssueLabel is struct
type IssueLabel struct {
	ID          uint64 `json:"id"`
	Name        string `json:"name"`
	Default     bool   `json:"default"`
	Description string `json:"description"`
}

//IssueAssignee is a struct
type IssueAssignee struct {
	Login     string `json:"login"`
	ID        uint64 `json:"id"`
	HTMLURL   string `json:"html_url"`
	Type      string `json:"type"`
	SiteAdmin bool   `json:"site_admin"`
}

//IssueDetails is struct
type IssueDetails struct {
	ID                uint64          `json:"id"`
	Number            int             `json:"number"`
	Title             string          `json:"title"`
	IssueUser         User            `json:"user"`
	Lables            []IssueLabel    `json:"labels"`
	State             string          `json:"state"`
	Locker            bool            `json:"locked"`
	Assignees         []IssueAssignee `json:"assignees"`
	NumberComments    uint64          `json:"comments"`
	CreatedAt         time.Time       `json:"created_at"`
	UpdatedAt         time.Time       `json:"updated_at"`
	ClosedAt          time.Time       `json:"closed_at"`
	AuthorAssociation string          `json:"author_association"`
	Body              string          `json:"body"`
}

//Comments is a struct
type Comments struct {
	CommentUser       User      `json:"user"`
	CreatedAt         time.Time `json:"created_at"`
	UpdatedAt         time.Time `json:"updated_at"`
	AuthorAssociation string    `json:"author_association"`
	Body              string    `json:"body"`
}
